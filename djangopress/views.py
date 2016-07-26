"""Views for djangopress"""
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import MonthArchiveView

from djangopress.models import Post, Option


class PostList(ListView):  # pylint:disable=too-many-ancestors
    """Home view."""
    model = Post
    context_object_name = 'posts'

    @staticmethod
    def get_paginate_by(queryset):
        posts, _ = Option.objects.get_or_create(name='posts_per_page',
                                                defaults={'value': '5'}
                                                )
        try:
            number_of_post = int(posts.value)
        except ValueError:
            number_of_post = 5
        return number_of_post


class PostDetail(DetailView):  # pylint: disable=too-many-ancestors
    """Post view."""
    model = Post


class MonthArchive(MonthArchiveView):  # pylint: disable=too-many-ancestors
    """Month archive view."""
    model = Post
    month_format = '%m'
    date_field = 'creation_date'
    context_object_name = 'posts'
