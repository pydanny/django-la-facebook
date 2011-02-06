=====
Goals
=====

Security is HARD.
Security is DANGEROUS.
Doing authentication via a third-party JavaScript library is STUPID.

Yet authentication via Facebook's JavaScript library is all over the place.

The better way would be to do authentication via Facebook-flavored OAUTH on the backend. With a well documented, testable project complete with working code examples. The working code examples should be in a dirt simple test project. The test project allows a developer to quickly analyze why facebook auth is failing without the complications of working in their entire system stack.

Our goals:

#. Good documentation that will build on readthedocs.org.
#. Proper logging for debug and intrusion analysis
#. Working test projects.
#. Working tests
#. Formal releases on PyPI