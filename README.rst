===========
README
===========


Add ``la_facebook`` to ``settings.INSTALLED_APPS``::

    settings.INSTALLED_APPS = (
        'django.contrib.admin',
        'la_facebook',
        ...
    )

Add the following to your settings::

    # to obtain these visit http://developers.facebook.com/setup/
    
    # DOUBLE CHECK THESE please!!!
    FACEBOOK_APP_ID = '124397597633470'
    FACEBOOK_API_KEY = '0d6acba060823bac2f93708d98d7e74a'
    FACEBOOK_APP_SECRET = 'cdd60917e6a30548b933ba91c48289bc'
    OAUTH_ACCESS_SETTINGS = {
        "facebook": {
            "keys": {
                "KEY": FACEBOOK_APP_ID,
                "SECRET": FACEBOOK_APP_SECRET,
            },
            "endpoints": {
                # OAuth 2.0 does not need a request token
                "access_token": "https://graph.facebook.com/oauth/access_token",
                "authorize": "https://graph.facebook.com/oauth/authorize",
                # Will need to redo the following
                "callback": "la_facebook.oauth.facebook_callback",
                # Probably too much power here - just need to have authentication
                "provider_scope": ["publish_stream"],            
            }
        }
    }


Add ``url(r"^la_facebook/", include("la_facebook.urls"))`` to your root urlconf.

Note: While using the test app `fb_la_test` you must use "http://localhost:8000" as your url, NOT 127.0.0.1. Facebook throws a wobbly when you try and use an IP address