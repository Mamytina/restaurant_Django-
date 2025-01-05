from django import template
from django.template.defaultfilters import stringfilter
register= template.Library()

@register.filter
@stringfilter
def first_cha(value):
    return value[0]
