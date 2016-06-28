"""Views for djangopress"""
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from djangopress.models import Post, Option


class HomeView(TemplateView):
    """Home view."""
    template_name = 'djangopress/index.html'

    def get_context_data(self, **kwargs):
        """Add title, tagline and posts to the template context."""
        context = super().get_context_data(**kwargs)
        title, _ = Option.objects.get_or_create(name='title',
                                                defaults={'value': 'Blog'}
                                                )
        tagline = 'Un blog mas'
        tagline, _ = Option.objects.get_or_create(name='tagline',
                                                  defaults={'value': tagline}
                                                  )
        context['title'] = title.value
        context['tagline'] = tagline.value
        context['posts'] = Post.objects.all()
        return context


class PostDetail(DetailView):  # pylint: disable=too-many-ancestors
    """Post view."""
    model = Post
