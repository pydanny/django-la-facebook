from django.conf import settings

from django.contrib.auth.models import User

from oauth_access.callback import AuthenticationCallback

from blarg.profiles.models import Profile

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

class BaseCallback(AuthenticationCallback):
    
    def handle_no_user(self, request, access, token, user_data):
        return self.create_user(request, access, token, user_data)
    
    def redirect_url(self, request):
        return get_default_redirect(request)

class FacebookCallback(BaseCallback):
    
    def create_user(self, request, access, token, user_data):
        identifier = self.identifier_from_data(user_data)
        username = str(identifier)
        if User.objects.filter(username=username).count():
            user = User.objects.get(username=username)
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                profile = None
        else:
            user = User(username=str(identifier))
            user.set_unusable_password()
            user.save()
            profile = None

        # TODO - customize it so it does the profiles better
        if not profile:
            profile = Profile.objects.create(
                user = user,
            )
            profile.save()
        self.login_user(request, user)
        return user    

    def fetch_user_data(self, request, access, token):
        url = "https://graph.facebook.com/me"
        return access.make_api_call("json", url, token)

    def identifier_from_data(self, data):
        # @@@ currently this is being used to make/lookup users and we don't
        # want a clash between services. need to look into the more.
        return "fb-%s" % data["id"]        
        
facebook_callback = FacebookCallback()