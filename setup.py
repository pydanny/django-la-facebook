from distutils.core import setup

setup(
    name = "django-la-facebook",
    version = "0.1.alpha",
    author = "pydanny",
    author_email = "pydanny@pydanny.com",
    description = "Definitive facebook auth for Django",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/pydanny/django-la-facebook",
    packages = [
        "la_facebook",
        "la_facebook.templatetags",
        "la_facebook.utils",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)