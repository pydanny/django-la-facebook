========
Settings
========

This document describes the settings needed by la_facebook.

FACEBOOK_ACCESS_SETTINGS this is the only setting required. It is a dictionary
of app specific settings as follows:

FACEBOOK_APP_ID - this is a key that uniquely identifies your Facebook app, in
the common case, the Facebook app will be your project or site.  

FACEBOOK_APP_SECRET - This secret is used in generating the authenticated
token.  Both the key and the secret are available through the `Facebook's Developer app <http://www.facebook.com/developers>`_.

CALLBACK (optional) - this is a dotted module path string (similar to using a string for
a view) that points to a subclass of la_facebook.callbacks.default. The default
value is "la_facebook.callbacks.default.default_facebook_callback"

PROVIDER_SCOPE (optional) - a list, of strings, of permissions to ask for.
The list of these is `here <http://developers.facebook.com/docs/authentication/permissions/>_`

LOG_LEVEL (optional) - A string value containing one of standard python logging
levels of DEBUG, INFO, WARNING, ERROR or CRITICAL. Defaults to "ERROR", which 
should be relatively quiet.

LOG_FILE (optional) - The path to a file that will received appended logging 
information.  By default, logged messages will print to stdout.

Example::
    
    FACEBOOK_ACCESS_SETTINGS = {
            "FACEBOOK_APP_ID": FACEBOOK_APP_ID,
            "FACEBOOK_APP_SECRET": FACEBOOK_APP_SECRET,
            # The following keys are optional
            # "CALLBACK": "la_facebook.callbacks.default.default_facebook_callback",
            # "PROVIDER_SCOPE": "email,read_stream",
            # "LOG_LEVEL": "DEBUG",
            # "LOG_FILE": "/tmp/la_facebook.log",
    }
