from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from la_facebook.access import OAuthAccess
from la_facebook.exceptions import MissingToken


def facebook_login(request, redirect_field_name="next",
                        redirect_to_session_key="redirect_to"):
    access = OAuthAccess()
    token = None
    if hasattr(request, "session"):
        request.session[redirect_to_session_key] = request.GET.get(redirect_field_name)
    return HttpResponseRedirect(access.authorization_url(token))


def facebook_callback(request):
    ctx = RequestContext(request)
    access = OAuthAccess()
    # TODO: Check to make sure the session cookie is setting correctly
    unauth_token = request.session.get("unauth_token", None)
    try:
        auth_token = access.check_token(unauth_token, request.GET)
    except MissingToken:
        ctx.update({"error": "token_missing"})
    else:
        if auth_token:
            return access.callback(request, access, auth_token)
        else:
            # @@@ not nice for OAuth 2
            ctx.update({"error": "token_mismatch"})
    return render_to_response("la_facebook/fb_error.html", ctx)


def finish_signup(request):
    access = OAuthAccess()
    return access.callback.finish_signup(request)
