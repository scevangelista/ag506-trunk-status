import html

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