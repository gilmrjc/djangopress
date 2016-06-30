"""Views for djangopress"""
from django.views.generic import ListView
from django.views.generic.detail import DetailView

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
    template_name = 'djangopress/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4


class PostDetail(DjangoPressMixin,  # pylint: disable=too-many-ancestors
                 DetailView):
    """Post view."""
    model = Post
