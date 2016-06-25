
from django.conf import settings
from django.views import generic
from django.shortcuts import render

from blog.models import Post, Option

def home(request):
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
    return render(request, 'blog/index.html', {'title': title,
                                              'tagline': tagline, 
                                              'posts': posts,
                                             })


class PostDetail(generic.detail.DetailView):
    context_object_name = 'post'
    date_field = 'creation_date'
    month_format = '%m'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_url = self.request.build_absolute_uri(self.request.path)
        context.update({'post_url': post_url})
