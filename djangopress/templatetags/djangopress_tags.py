"""Templatetags for djangopress."""
import re
from datetime import date
from collections import defaultdict

from django import template
from django.utils.html import escape
from django.utils.encoding import force_text
from django.utils.text import normalize_newlines
from django.utils.safestring import SafeData, mark_safe
from django.template.defaultfilters import stringfilter

from djangopress.models import Post, Category


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


@register.inclusion_tag('djangopress/tags/archive_list.html')
def archive_list():
    """List post by date"""
    posts = Post.objects.all()
    years_dictionary = defaultdict(set)
    for post in posts:
        year = post.creation_date.year
        month = post.creation_date.month
        years_dictionary[year].add(month)
    years = {}
    for year, months in years_dictionary.items():
        year = str(year)
        years[year] = []
        for month in months:
            years[year].append(date(int(year), month, 1))
    for year in years:
        years[year].sort(reverse=True)
    return {'years': years}


@register.inclusion_tag('djangopress/tags/category_list.html')
def category_list():
    """List the categories in the blog."""
    categories = Category.objects.all()
    return {'categories': categories}
