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
        expected_callback_endpoint = load_path_attr(oauth._obtain_setting("endpoints", "callback"))
        self.assertEquals(callback_endpoint,expected_callback_endpoint)
