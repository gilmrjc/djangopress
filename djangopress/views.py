"""Views for djangopress"""
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import MonthArchiveView

from djangopress.models import Post, Option


class DjangoPressMixin(object):  # pylint: disable=too-few-public-methods
    """Mixin to load the basic information to template context."""
    def get_context_data(self, **kwargs):
        """Add title and tagline to the template context."""
        context = super(DjangoPressMixin, self).get_context_data(**kwargs)
        title, _ = Option.objects.get_or_create(name='title',
                                                defaults={'value': 'Blog'}
                                                )
        tagline = 'Un blog mas'
        tagline, _ = Option.objects.get_or_create(name='tagline',
                                                  defaults={'value': tagline}
                                                  )
        context['title'] = title.value
        context['tagline'] = tagline.value
        return context


class HomeView(DjangoPressMixin,  # pylint:disable=too-many-ancestors
               ListView):
    """Home view."""
    template_name = 'djangopress/home.html'
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


class PostDetail(DjangoPressMixin,  # pylint: disable=too-many-ancestors
                 DetailView):
    """Post view."""
    model = Post


class MonthArchive(DjangoPressMixin,  # pylint: disable=too-many-ancestors
                   MonthArchiveView
                   ):
    """Month archive view."""
    model = Post
    month_format = '%m'
    date_field = 'creation_date'
    context_object_name = 'posts'
