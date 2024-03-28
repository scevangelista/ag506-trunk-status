import html
import json
import requests
from urllib.parse import urlparse


# Checks received parameters and minimally validates
def validateParams( url, user, password ):
    url = html.escape( url )
    user = html.escape( user )
    
    if( len( user ) < 5 ):
        return { "sucess": False, "message": "The user must have more than 4 characters" }
    
    if( len( password ) < 5 ):
        return { "sucess": False, "message": "The password must have more than 4 characters" }
    
    oUrl = urlparse( url )
    if( not( oUrl.geturl() ) ):
        return { "sucess": False, "message": "The url is invalid" }
    
    return { "sucess": True, "url": oUrl.geturl(), "user": user, "password": password }


# Query the equipment and return normalized data
def getData( url, user, password ):

    resVal = validateParams( url, user, password )
    if not( resVal["sucess"] ):
        return json.dumps( resVal )

    # Authenticate to the device and save the session for future requests
    session = requests.Session()
    resAuth = session.post( resVal["url"] + "/app/do.login", { "username": user, "password": password } )

    if resAuth.status_code == 200:

        # Get page with trunk status
        resData = session.get( resVal["url"] + "/app/do.status" )

        if resData.status_code == 200:

        else:
            return {"status": False, "message": "Getting status page error"}

    else:
        return {"status": False, "message": "Authentication error"}