from django.conf.urls.defaults import *


urlpatterns = patterns("la_facebook.views",
    url(
        regex = r"^login/(?P<service>\w+)/$",
        view = "facebook_login",
        name = "la_facebook_login",
    ),
    url(
        regex = r"^callback/(?P<service>\w+)/$",
        view = "facebook_callback",
        name = "la_facebook_callback"
    ),
    url(
        regex = r"^finish_signup/(?P<service>\w+)/$",
        view = "finish_signup",
        name = "la_facebook_finish_signup"
    )
)