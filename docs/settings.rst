========
Settings
========

This document describes the settings needed by la_facebook.

FACEBOOK_ACCESS_SETTINGS this is the only setting required. It is a dicitonary
of app specific settings as follows:


FACEBOOK_APP_ID - this is a key that uniquely identifies your Facebook app, in
the common case, the Facebook app will be your project or site.  

FACEBOOK_APP_SECRET - This secret is used in generating the authenticated
token.  Both the key and the secret are available through the `Facebook's Developer app <http://www.facebook.com/developers>`.

CALLBACK (optional) - this is a dotted module path string (similar to using a string for
a view) that points to a subclass of la_facebook.callbacks.default

PROVIDER_SCOPE (optional) - a comma delimited string of permissions to ask for.
The list of these is `here <http://developers.facebook.com/docs/authentication/permissions/>`
