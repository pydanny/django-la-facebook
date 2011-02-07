==========
Background
==========

This documents provides a quick overview of the events involved in
authenticating a user against facebook.

Facebook has had various authentication methods in the past (Facebook Connect),
but has currently standardized on using `OAuth 2 Protocol
<http://tools.ietf.org/pdf/draft-ietf-oauth-v2-12.pdf>`_.

Facebook's `own documentation
<http://developers.facebook.com/docs/authentication>`_ does a reasonable job of
explaining the process, but it is summarized here. Facebook offers two
workflows for user authentication, client (javascript) based, and server side.
This project aims to provide a Python based, server side option.

There are three parts to Facebook's authentication:

   - user authentication (ensures that the user is who they say they are) 
   - app authorization (ensures that the user knows exactly what data and capabilities they are providing to your site) 
   - app authentication (ensures that the user is giving their information to your app and not someone else)

Facebook will only authenticate a user in relation to a specific app, there is
no "just authorize the user" option. In our case, the "app" that is
authenticated is your entire Django project or site, not a specific Django app.
For Facebook to associate your site with the authentication, you will need an
app ID from `Facebook's Developer app <http://www.facebook.com/developers>`_,
which is placed in your Django settings file.

A user is authenticated to facebook, and your app in one step.  The first time
this happens, the user will be prompted to approve the level of access you are
asking for.  By default and at a minimum this includes the basic info that is
publicly available about the user on Facebook. (for additional permissions, see
the documentation for settings). The permissions approved will be global to all
your Django apps in your Django project.

Once your site is authorized by Facebook, an authorization token is stored in
a model associated with a Django user (which by default is created if needed).
That user that will then be the authenticated user for subsequent requests
(request.user).
