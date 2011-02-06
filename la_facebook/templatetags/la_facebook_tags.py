from django import template

from la_facebook.models import UserAssociation

register = template.Library()


@register.filter
def authed_via(user):
    if user.is_authenticated():
        try:
            assoc = UserAssociation.objects.get(user=user)
        except UserAssociation.DoesNotExist:
            return False
        return assoc.expired()
    else:
        return False
