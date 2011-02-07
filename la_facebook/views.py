from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from la_facebook.access import OAuthAccess
from la_facebook.exceptions import MissingToken
from la_facebook.la_fb_logging import logger


def facebook_login(request, redirect_field_name="next",
                        redirect_to_session_key="redirect_to"):
    """
        1. access OAuth
        2. set token to none
        3. store and redirect to authorization url
        4. redirect to OAuth authorization url
    """
    
    access = OAuthAccess()
    token = None
    if hasattr(request, "session"):
        logger.debug("la_facebook.views.facebook_login: request has session")
        request.session[redirect_to_session_key] = request.GET.get(redirect_field_name)
    return HttpResponseRedirect(access.authorization_url(token))


def facebook_callback(request):
    """
        1. define RequestContext
        2. access OAuth
        3. check session
        4. autheticate token
        5. raise exception if missing token
        6. return access callback
        7. raise exception if mismatch token
        8. render error 
    """
    
    ctx = RequestContext(request)
    access = OAuthAccess()
    # TODO: Check to make sure the session cookie is setting correctly
    unauth_token = request.session.get("unauth_token", None)
    try:
        auth_token = access.check_token(unauth_token, request.GET)
    except MissingToken:
        ctx.update({"error": "token_missing"})
        logger.error('la_facebook.views.facebook_login: missing token')
    else:
        if auth_token:
            return access.callback(request, access, auth_token)
        else:
            # @@@ not nice for OAuth 2
            ctx.update({"error": "token_mismatch"})
            logger.error('la_facebook.views.facebook_callback: token mismatch'\
                    ', error getting token, or user denied FB login')
    return render_to_response("la_facebook/fb_error.html", ctx)


def finish_signup(request):
    """
        1. access OAuth
        2. return callback url and finish signup
    """
    
    access = OAuthAccess()
    return access.callback.finish_signup(request)
