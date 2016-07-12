"""Templatetags for djangopress."""
from django import template

register = template.Library()

@register.inclusion_tag('djangopress/tags/archive_list.html')
def archive_list():
    """List post by date"""
    return {}
