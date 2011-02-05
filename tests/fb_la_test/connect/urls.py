from django.conf.urls.defaults import *

urlpatterns = patterns('fb_la_test.connect.views',
    url(r'^/?$', "test_index", name="index"),
    url(r'^after/?$', "after", name="after"),
    url(r"^la_facebook/", include("la_facebook.urls")),
)