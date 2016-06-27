"""Views for djangopress"""

from django.views import generic
from django.shortcuts import render

from djangopress.models import Post, Option

def home(request):
    """Home view."""
    title, _ = Option.objects.get_or_create(name='title',
                                            defaults={'value': 'Blog'}
                                           )
    tagline = 'Un blog mas'
    tagline, _ = Option.objects.get_or_create(name='tagline',
                                              defaults={'value': tagline}
                                             )
    title = title.value
    tagline = tagline.value
    posts = Post.objects.all()
    return render(request, 'djangopress/index.html', {'title': title,
                                                      'tagline': tagline,
                                                      'posts': posts,
                                                     })


class PostDetail(generic.detail.DetailView): # pylint: disable=too-many-ancestors
    """Post view."""
    model = Post
