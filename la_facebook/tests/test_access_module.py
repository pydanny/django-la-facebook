from django.conf import settings
from django.test import TestCase

from la_facebook.access import OAuthAccess

class PropertyTests(TestCase):
    
    def test_key_in_settings(self):
        # test if there is a key
        oath = OAuthAccess()
        self.assertEquals(oath.key, "124397597633470")
        #self.assertRaises(NameError, runt_this)
        
    def test_callback_url(self):
        
        pass
        
    def test_callback(self):
        pass