from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth.models import User

from django.conf import settings


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


class Callback(object):
    
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
        raise NotImplementedError()
    
    def lookup_user(self, request, access, user_data):
        return access.lookup_user(identifier=self.identifier_from_data(user_data))
    
    def redirect_url(self, request):
        raise NotImplementedError()


class FacebookCallback(Callback):

    def handle_no_user(self, request, access, token, user_data):
        return self.create_user(request, access, token, user_data)
        
    def handle_unauthenticated_user(self, request, user, access, token, user_data):
        self.login_user(request, user)
        
    def redirect_url(self, request):
        return get_default_redirect(request)

    def update_profile_from_graph(self, request, access, token, profile):
           user_data = self.fetch_user_data(request, access, token)
           for k,v in user_data.items():
               if hasattr(profile, k):
                   setattr(profile, k, v)
           return profile

    def create_user(self, request, access, token, user_data):
       identifier = self.identifier_from_data(user_data)
       username = str(identifier)
       if User.objects.filter(username=username).count():
           user = User.objects.get(username=username)
       else:
           user = User(username=str(identifier))
           user.set_unusable_password()
           user.save()

       # start Profile handling code
       # start Profile handling code
       # start Profile handling code          
       if hasattr(settings, settings.AUTH_PROFILE_MODULE):
           profile_model = get_model(settings.AUTH_PROFILE_MODULE)
           try:
               profile = user.get_profile()
           except profile_model.DoesNotExist:
               # TODO - provide base code for this to be extended by developer
               # create the profile record here
               profile = profile_model.objects.create(
                   user = user,
               )
           profile = self.update_profile_from_graph(request, access, token, profile)
           profile.save()

       else:
           # Do nothing because users have no site profile defined
           # TODO - should we pass a warning message? Raise a SiteProfileNotAvailable error?
           pass

       # end Profile handling code
       # end Profile handling code
       # end Profile handling code                            

       self.login_user(request, user)
       return user

    def fetch_user_data(self, request, access, token):
        url = "https://graph.facebook.com/me"
        return access.make_api_call("json", url, token)

    def identifier_from_data(self, data):
        # @@@ currently this is being used to make/lookup users and we don't
        # want a clash between services. need to look into the more.
        return "fb-%s" % data["id"]
        
    def login_user(self, request, user):
        user.backend = "django.contrib.auth.backends.ModelBackend"
        login(request, user)