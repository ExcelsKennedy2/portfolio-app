from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter
def slugify_class(value):
    return slugify(value)
