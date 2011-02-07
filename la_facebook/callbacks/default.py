from django.db.models import get_model

from django.contrib.auth.models import User

from django.conf import settings

from la_facebook.la_fb_logging import logger
from la_facebook.callbacks.base import (BaseFacebookCallback, 
        get_default_redirect, FACEBOOK_GRAPH_TARGET)

class DefaultFacebookCallback(BaseFacebookCallback):
    
    def fetch_user_data(self, request, access, token):
        url = FACEBOOK_GRAPH_TARGET
        return access.make_api_call("json", url, token)
    
    def lookup_user(self, request, access, user_data):
        return access.lookup_user(identifier=self.identifier_from_data(user_data))
    
    def redirect_url(self, request):
        return get_default_redirect(request)

    def handle_no_user(self, request, access, token, user_data):
        return self.create_user(request, access, token, user_data)

    def handle_unauthenticated_user(self, request, user, access, token, user_data):
        self.login_user(request, user)
        
    def update_profile_from_graph(self, request, access, token, profile):
        user_data = self.fetch_user_data(request, access, token)
        for k, v in user_data.items():
            if k !='id' and hasattr(profile, k):
                setattr(profile, k, v)
                logger.debug("DefaultFacebookCallback.update_profile_from_graph"\
                        ": updating profile %s to %s" % (k,v))
        return profile 
           
    def create_profile(self, request, access, token, user):

        if hasattr(settings, 'AUTH_PROFILE_MODULE'):
            profile_model = get_model(*settings.AUTH_PROFILE_MODULE.split('.'))

            profile, created = profile_model.objects.get_or_create(
              user = user,
            )
            profile = self.update_profile_from_graph(request, access, token, profile)
            profile.save()

        else:
            # Do nothing because users have no site profile defined
            # TODO - should we pass a warning message? Raise a SiteProfileNotAvailable error?
            logger.warning("DefaultFacebookCallback.create_profile: unable to" \
                    "create/update profile as no AUTH_PROFILE_MODULE setting" \
                    "has been defined")
            pass

    def create_user(self, request, access, token, user_data):
        identifier = self.identifier_from_data(user_data)
        username = str(identifier)
        if User.objects.filter(username=username).count():
            logger.warning("DefaultFacebookCallback.create_user: A user for" \
                    "was already found, when asked to create a user for %s" 
                    % username)
            user = User.objects.get(username=username)
        else:
            user = User(username=str(identifier))
            user.set_unusable_password()
            user.save()
            logger.debug("DefaultFacebookCallback.create_user: new django" \
                    "user created for %s" % username)

        self.create_profile(request, access, token, user)

        self.login_user(request, user)
        return user

default_facebook_callback = DefaultFacebookCallback()
