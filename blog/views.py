import urllib
from django.conf import settings
from django.views import generic
from blog.models import Post

class PostDetail(generic.dates.DateDetailView):
    context_object_name = 'post'
    date_field = 'creation_date'
    month_format = '%m'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_url = self.request.build_absolute_uri(self.request.path)
        context.update({'post_url': post_url})

    def get_object(self):
        self.kwargs['slug'] = urllib.parse.quote(self.kwargs['slug'].encode('utf-8')).lower()
        return super(PostDetail, self).get_object()
