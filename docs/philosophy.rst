==========
Philosophy
==========

For a customer I needed to do Facebook authentication on a new Django project. I went to the Django Packages Facebook Authentication Grid and figured I would plug it in, set some keys, and go! Facebook authentication is a common client requirement, and this must have been solved many times over, right?

Unfortunately, most (I'm still going through them) of the listed packages worry me. Security is HARD. Security is DANGEROUS. Since Facebook auth is a common requirement I shouldn't be forced to roll my own authentication or hack through someone else's implementation to get things working.

Yet many of the packages listed in the grid above lack documentation or what exists is outdated. Some of them simply drop errors or seem to intentionally obfuscate them (I won't name anyone YET because I want to give people a chance to correct these issues). Finally, I've yet to find any with any sort of logging to help diagnose possible intrusions or just as a way to see what is happening when you have trouble hooking up things.

I understand that Facebook is a moving target. But on the other hand, shouldn't updates to these things be in place?

So what do I want in a Django app that does Facebook authentication?
Documentation that will build on readthedocs.org.
Use of the logging module for diagnosis.
Sample project with a working example of hitting a dummy app (call it stupid-test-for-pydanny if you like) on Facebook provided by the project manager.
Proper packaging on PyPI
In the spirit of things if your project does this I'm willing to try it out and blog about it. I'm also going to sprint on this issue during Saturday's Hackathon at Cartwheel HQ.