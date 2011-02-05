from django.test import TestCase

class LaFacebookTestCase(TestCase):
    
    def response_200(self, response):
        self.assertEqual(response.status_code, 200)

    def response_302(self, response):
        self.assertEqual(response.status_code, 302)


