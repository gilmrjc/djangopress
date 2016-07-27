"""Templatetags for blog."""
from datetime import date
from collections import defaultdict

from django import template

from ..models import Post, Category


register = template.Library()


@register.inclusion_tag('blog/tags/archive_list.html')
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


@register.inclusion_tag('blog/tags/category_list.html')
def category_list():
    """List the categories in the blog."""
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('blog/tags/recent_posts.html')
def recent_posts():
    """List the recent posts."""
    posts = Post.objects.all()[:5]
    return {'posts': posts}
