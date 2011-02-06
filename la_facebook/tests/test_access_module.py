from django.conf import settings
from django.test import TestCase
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from la_facebook.access import OAuthAccess
from la_facebook.utils.loader import load_path_attr

class PropertyTests(TestCase):

    def test_key_in_settings(self):
        # test if there is a key
        oauth = OAuthAccess()
        self.assertEquals(oauth.key, "124397597633470")
    
    def test_secret_in_settings(self):
        oauth = OAuthAccess()
        self.assertEquals(oauth.secret, "cdd60917e6a30548b933ba91c48289bc")
    
    def test_access_token_url(self):
        oauth = OAuthAccess()
        access_token_endpoint = oauth.access_token_url
        expected_endpoints_url = "https://graph.facebook.com/oauth/access_token"
        self.assertEquals(access_token_endpoint,expected_endpoints_url)
    
    def test_authorize_url(self):
        oauth = OAuthAccess()
        authorize_url_endpoint = oauth.authorize_url
        expected_endpoint_url = "https://graph.facebook.com/oauth/authorize"
        self.assertEquals(authorize_url_endpoint,expected_endpoint_url)
    
    def test_provider_scope(self):
        oauth = OAuthAccess()
        provider_scope_endpoint = oauth.provider_scope
        expected_endpoint_url = None
        self.assertEquals(provider_scope_endpoint,expected_endpoint_url)
    
    def test_callback_url(self):
        oauth = OAuthAccess()
        callback_url = oauth.callback_url
        current_site = Site.objects.get(pk=settings.SITE_ID)
        base_url = "http://%s" % current_site.domain
        reversed_url = reverse("la_facebook_callback")
        expected_url = "%s%s" % (base_url, reversed_url)
        self.assertEquals(callback_url,expected_url)
    
    def test_callback(self):
        oauth = OAuthAccess()
        callback_endpoint = oauth.callback
        expected_callback_endpoint = load_path_attr(settings.FACEBOOK_ACCESS_SETTINGS["CALLBACK"])
        self.assertEquals(callback_endpoint,expected_callback_endpoint)
