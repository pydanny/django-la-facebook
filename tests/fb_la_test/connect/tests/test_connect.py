import httplib2

from fb_la_test.connect.tests.utils import LaFacebookTestCase

class TestConnection(LaFacebookTestCase):
    
        
    def test_login_first_stage(self):
        """ This test checks that we can touch facebook's oauth client"""
        
        url = "https://www.facebook.com/dialog/oauth?client_id={{ app_id }}&redirect_uri=http%3A//localhost%3A8000/after&scope=email,read_stream"
        h = httplib2.Http()
        resp, content = h.request(url, method="GET")
        
        print resp
        
        print "*"*80
        print "*"*80
        print "*"*80                
        
        print content        
        
    def test_authentication_after_facebook_authentication(self):
        pass
        
        
