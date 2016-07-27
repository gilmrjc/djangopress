"""Templatetags for djangopress."""
import re

from django import template
from django.utils.html import escape
from django.utils.encoding import force_text
from django.utils.text import normalize_newlines
from django.utils.safestring import SafeData, mark_safe
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(is_safe=True, needs_autoscape=True)
@stringfilter
def more(value, arg, autoescape=True):
    """Adds a "Read more" tag in the post preview."""
    autoescape = autoescape and not isinstance(value, SafeData)
    if autoescape:
        text = escape(value)
    text = re.split(r'<!--\s*more\s*-->', value)
    more_link = '<p><a href="%s" class="more-link">Read More</a><p>' % arg
    text = text[0] + more_link if len(text) > 1 else text[0]
    return mark_safe(text)


@register.filter(is_safe=True, needs_autoscape=True)
def linebreakshtml(value, autoescape=True):
    """
    Replaces double line breaks in HTML to a paragraph break (``</p>``).
    This tag ignores single line breaks.
    """
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(force_text(value))
    if autoescape:
        value = escape(value)
    paras = re.split('\n{2,}', value)
    paras = ['<p>%s</p>' % p for p in paras]
    return mark_safe(''.join(paras))
