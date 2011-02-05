from django.conf import settings
from django.shortcuts import render_to_response

def test_index(request):
    context_dict = {
        'app_id': settings.FACEBOOK_APP_ID,
    }
    
    return render_to_response('index.html', context_dict)
    
def after(request):
    context_dict = {
        'code': request.GET.get('code', None)
    }
    
    return render_to_response('after.html', context_dict)