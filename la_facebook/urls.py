from django.conf.urls.defaults import *


urlpatterns = patterns("la_facebook.views",
    url(
        regex = r"^login/?$",
        view = "facebook_login",
        name = "la_facebook_login",
    ),
    url(
        regex = r"^callback/?$",
        view = "facebook_callback",
        name = "la_facebook_callback"
    ),
    url(
        regex = r"^finish_signup/?$",
        view = "finish_signup",
        name = "la_facebook_finish_signup"
    )
)