"""Templatetags for djangopress."""
from datetime import date
from collections import defaultdict

from django import template

from djangopress.models import Post, Category


register = template.Library()


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
    return {'years': years}


@register.inclusion_tag('djangopress/tags/category_list.html')
def category_list():
    """List the categories in the blog."""
    categories = Category.objects.all()
    return {'categories': categories}
