"""Templatetags for djangopress."""
from datetime import date
from collections import defaultdict

from django import template

from djangopress.models import Post


register = template.Library()


@register.inclusion_tag('djangopress/tags/archive_list.html')
def archive_list():
    """List post by date"""
    posts = Post.objects.all()
    dict = defaultdict(set)
    for post in posts:
        year = post.creation_date.year
        month = post.creation_date.month
        dict[year].add(month)
    years = {}
    for year, months in dict.items():
        year = str(year)
        years[year] = []
        for month in months:
            years[year].append(date( int(year), month, 1))
    return years
