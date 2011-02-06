from django.conf.urls.defaults import *

urlpatterns = patterns('test_project.connect.views',
    url(r'^/?$', "test_index", name="index"),
    url(r'^after/?$', "after", name="after"),
)