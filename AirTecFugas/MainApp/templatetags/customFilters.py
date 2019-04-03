from django.template.defaulttags import register
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import Group


@register.filter
def is_in_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


