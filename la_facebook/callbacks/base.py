from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import get_model

from django.contrib.auth import login
from django.contrib.auth.models import User

from django.conf import settings

LA_FACEBOOK_PROFILE_PREFIX = 'fb-'
FACEBOOK_GRAPH_TARGET = "https://graph.facebook.com/me"


def get_default_redirect(request, fallback_url=settings.LOGIN_REDIRECT_URL, redirect_field_name="next", session_key_value="redirect_to"):
   """
   Returns the URL to be used in login procedures by looking at different
   values in the following order:

   - a REQUEST value, GET or POST, named "next" by default.
   - LOGIN_REDIRECT_URL - the URL in the setting
   - LOGIN_REDIRECT_URLNAME - the name of a URLconf entry in the settings
   """

   redirect_to = request.REQUEST.get(redirect_field_name)
   if not redirect_to:
       # try the session if available
       if hasattr(request, "session"):
           redirect_to = request.session.get(session_key_value)
   # light security check -- make sure redirect_to isn't garabage.
   if not redirect_to or "://" in redirect_to or " " in redirect_to:
       redirect_to = fallback_url
   return redirect_to


class BaseFacebookCallback(object):
    
    def __call__(self, request, access, token):
        if not request.user.is_authenticated():
            authenticated = False
            user_data = self.fetch_user_data(request, access, token)
            user = self.lookup_user(request, access, user_data)
            if user is None:
                ret = self.handle_no_user(request, access, token, user_data)
                # allow handle_no_user to create a user if need be
                if isinstance(ret, User):
                    user = ret
            else:
                ret = self.handle_unauthenticated_user(request, user, access, token, user_data)
            if isinstance(ret, HttpResponse):            
                return ret
        else:
            authenticated = True
            user = request.user
        redirect_to = self.redirect_url(request)
        if user:
            kwargs = {}
            if not authenticated:
                kwargs["identifier"] = self.identifier_from_data(user_data)
            access.persist(user, token, **kwargs)

        return redirect(redirect_to)
    
    def fetch_user_data(self, request, access, token):
        raise NotImplementedError("Callbacks must have a fetch_user_data method")
    
    def lookup_user(self, request, access, user_data):
        raise NotImplementedError("Callbacks must have a lookup_user method")
    
    def redirect_url(self, request):
        raise NotImplementedError("Callbacks must have a redirect_url method")

    def handle_no_user(self, request, access, token, user_data):
        raise NotImplementedError("Callbacks must have a handle_no_user method")

    def handle_unauthenticated_user(self, request, user, access, token, user_data):
        raise NotImplementedError("Callbacks must have a handle_unauthenticated_user method")
        
    def update_profile_from_graph(self, request, access, token, profile):
        raise NotImplementedError("Callbacks must have a update_profile_from_graph method")
        
    def create_profile(self, request, access, token, user):
        raise NotImplementedError("Callbacks must have a create_profile method")               
           
    def create_user(self, request, access, token, user_data):
        raise NotImplementedError("Callbacks must have a create_user method")       
      
    def identifier_from_data(self, data):
        # @@@ currently this is being used to make/lookup users and we don't
        # want a clash between services. need to look into the more.
        return LA_FACEBOOK_PROFILE_PREFIX + data["id"]

    def login_user(self, request, user):
        user.backend = "django.contrib.auth.backends.ModelBackend"
        login(request, user)               
