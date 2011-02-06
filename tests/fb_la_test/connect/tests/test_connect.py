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
        
        form_data = dict(
            charset_test=unicode(r"&euro;,&acute;,\xe2,\xc2,\xd0,\xd0", "utf-8"),
            lsd="IuLli",
            next="http://www.facebook.com/connect/uiserver.php?method=permissions.request&amp;app_id=124397597633470&amp;display=page&amp;redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fafter&amp;response_type=code&amp;fbconnect=1&amp;perms=email%2Cread_stream&amp;from_login=1",
            api_key="124397597633470",
            return_session="0",
            cancel_url="http://localhost:8000/after?error_reason=user_denied&amp;error=access_denied&amp;error_description=The+user+denied+your+request.",
            legacy_return="1",
            display="page",
            session_key_only="0",
            skip_api_login="1",
            trynum="1",
            email="",
            pass1="",
            persistent="1",
            default_persistent="0",
            Login="login"
        )
        form_data["pass"] = form_data["pass1"]
        del form_data["pass1"]

        
        self.assertRaises(TypeError, 
                            h.request,
                            "http://www.facebook.com/connect/uiserver.php",
                            body=form_data
        )
        
    def test_authentication_after_facebook_authentication(self):
        pass
