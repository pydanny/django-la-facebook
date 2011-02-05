from django.conf import settings
from django.shortcuts import render_to_response
from la_facebook.models import UserAssociation
import httplib2
import json

def test_index(request):
    context_dict = {
        'app_id': settings.FACEBOOK_APP_ID,
    }
    
    return render_to_response('index.html', context_dict)
    
def after(request):
    # Let's prove facebook's creepy stalker-ware is working
    # TODO: Needs a lot of validation
    ua = UserAssociation.objects.get(user=request.user)
    url = "https://graph.facebook.com/me?access_token=%s" % ua.token
    h = httplib2.Http()
    print url
    resp, content = h.request(url)
    
    profile_data = json.loads(content)
    
    print profile_data
    if 'error' in profile_data:
        context_dict = {
            'error': profile_data['error'].get('message')
        }
    else:
        context_dict = {
            'name': profile_data['name']
        }
    
    return render_to_response('after.html', context_dict)