class FacebookSettingsKeyError(KeyError):
    """ Expect to see at least:
    
    FACEBOOK_ACCESS_SETTINGS = {
        "keys": {
            "FACEBOOK_APP_ID": <MY_FACEBOOK_APP_ID>,
            "FACEBOOK_APP_SECRET": <MY_FACEBOOK_APP_SECRET>,
        },
        "endpoints": {
            # Will need to redo the following
            "callback": "fb_la_test.oauth.facebook_callback",
            # Probably too much power here - just need to have authentication
        }
    }
    """
    pass


class NotAuthorized(Exception):
    pass


class MissingToken(Exception):
    pass


class UnknownResponse(Exception):
    pass


class ServiceFail(Exception):
    pass
