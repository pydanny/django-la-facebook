from django.conf.urls.defaults import *
from django.contrib import admin 
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^', include('test_project.connect.urls')),
    url(r"^la_facebook/", include("la_facebook.urls")),
    url(r'^admin/(.*)', admin.site.root)
)
