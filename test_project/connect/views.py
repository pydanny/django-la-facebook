from django.conf import settings
from django.shortcuts import render_to_response
from fb_la_test.connect.models import Profile

def test_index(request):
    context_dict = {
        'app_id': settings.FACEBOOK_APP_ID,
    }
    
    return render_to_response('index.html', context_dict)
    
def after(request):
    # Let's prove facebook's creepy stalker-ware is working
    # TODO: Needs a lot of validation
    context_dict = {}
    
    if hasattr(request, 'user'):
        context_dict['user'] = request.user
        try:
            context_dict['profile'] = request.user.get_profile()
        except Profile.DoesNotExist:
            pass
        
    
    return render_to_response('after.html', context_dict)