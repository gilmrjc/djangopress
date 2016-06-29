"""Djangopress' Urls """
from django.conf.urls import url, include

from .views import HomeView, PostDetail

app_name = 'djangopress'  # pylint: disable=invalid-name
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post/(?P<slug>[\w\d-]+)/$', PostDetail.as_view(), name='post'),
]
