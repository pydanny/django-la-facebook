from django.conf import settings

import httplib2

from fb_la_test.connect.tests.utils import LaFacebookTestCase

class TestConnection(LaFacebookTestCase):
    
        
    def test_login_first_stage(self):
        """ This test checks that we can touch facebook's oauth client"""
        
        # based off http://httplib2.googlecode.com/hg/doc/html
        
        url = "https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http%%3A//localhost%%3A8000/after&scope=email,read_stream" % settings.FACEBOOK_APP_ID
        h = httplib2.Http()
        resp, content = h.request(url, method="GET")
        
        
        print url     
        x = file('url', 'w')   
        x.write(url)

        print "*"*40
        print "*"*40
        print "*"*40                

        
        print resp
        
        print "*"*40
        print "*"*40
        print "*"*40                
        
        print content      
        
        form_data = dict(
            charset_test="€,´,€,´,水,Д,Є",
            lsd="t9rTc"
        )

        
        resp, content = h.request(url, method="POST", body=form_data)  
        
    def test_authentication_after_facebook_authentication(self):
        pass
        
        
