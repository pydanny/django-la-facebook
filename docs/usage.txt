=====
Usage
=====

Get ``django-la-facebook`` into your python path::

    pip install django-la-facebook
    
Add ``la_facebook`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'la_facebook',
        ...
        )
    
Add ``la_facebook`` to your root urlconf (urls.py)::

    urlpatterns = patterns('',
        ...,
        url(r"^la_facebook/", include("la_facebook.urls")),
        ...,        
    )

TODO: add in the template wiring instructions