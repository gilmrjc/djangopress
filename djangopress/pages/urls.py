"""Pages' URLs."""
from django.conf.urls import url

from .views import PageDetail


urlpatterns = [
    url(r'^(?P<slug>[\w\d-]+)/$', PageDetail.as_view(), name='page'),
]
