from django.template.defaulttags import register
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import Group
from django import template
from django.contrib.humanize.templatetags.humanize import intcomma


@register.filter
def is_in_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


@register.filter
def prepend_dollars(dollars):
    if dollars:
        dollars = round(float(dollars), 2)
        return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
    else:
        return ''

