import base64
import html
import json
import requests

from bs4 import BeautifulSoup
from redis import Redis
from urllib.parse import urlparse


# Checks received parameters and minimally validates
def validateParams(url, user, password):
    url = html.escape(url)
    user = html.escape(user)

    if len(user) < 5:
        return {"sucess": False, "message": "The user must have more than 4 characters"}

    if len(password) < 5:
        return {"sucess": False, "message": "The password must have more than 4 characters"}

    oUrl = urlparse(url)
    if not (oUrl.geturl()):
        return {"sucess": False, "message": "The url is invalid"}

    return {"sucess": True, "url": oUrl.geturl(), "user": user, "password": password}


# Query the equipment and return normalized data
def getData(url, user, password):

    resVal = validateParams(url, user, password)
    if not (resVal["sucess"]):
        return json.dumps(resVal)

    # Redis for response cache
    redis = Redis(host='cache', port=6379)
    redisKey = (base64.b64encode((url+user+password).encode())).decode()
    cachedRes = redis.get(redisKey)

    if cachedRes:
        return json.loads(cachedRes)
    else:
        # Authenticate to the device and save the session for future requests
        session = requests.Session()
        resAuth = session.post(resVal["url"]+"/app/do.login", {"username": user, "password": password})

    # Continue if session is validate
    if resAuth.status_code == 200:

        # Get page with trunk status
        resData = session.get(resVal["url"]+"/app/do.status")

        if resData.status_code == 200:

            # Read page and create response
            page = BeautifulSoup(resData.text, "html.parser")
            trunks = page.findAll("div", attrs={"class": "e1_status"})

            res = {}
            res["status"] = True

            for trunk in trunks:

                data = {}
                data["name"] = (trunk.find( "span", attrs={ "class": "hr_text" } ).text).replace(" ", "_")
                data["alarm"] = trunk.find("table", attrs={"class": "e1_alarms"}).find("td").text

                for status in trunk.find("table", attrs={"class": "e1_stats"}).findAll("tr"):

                    details = status.findAll("td")

                    data[details[0].text.replace(" ", "_").lower()] = details[1].text
                    data[details[0].text.replace(" ", "_").lower()+"_total"] = details[2].text

                res[data["name"]] = data

                # Set cache
                redis.set(redisKey, json.dumps(res), ex=30)

            return res

        else:
            return {"status": False, "message": "Getting status page error"}

    else:
        return {"status": False, "message": "Authentication error"}
