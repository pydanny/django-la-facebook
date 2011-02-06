===========
README
===========

Dedicated facebook authentication for Django that does it via the backend and not javascript. Has lots of tests and a trivial-to-setup test project with working code.

The blog entry that started it all:

    http://pydanny.blogspot.com/2011/01/what-i-want-for-django-facebook-connect.html

Full Documentation:

    http://django-la-facebook.readthedocs.org/en/latest/index.html

Usage
-----

*Note: still in process of writing this down*

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