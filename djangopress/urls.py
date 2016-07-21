"""Djangopress' Urls """
from django.conf.urls import url

from .views import HomeView, PostDetail, MonthArchive

app_name = 'djangopress'  # pylint: disable=invalid-name
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)$',
        MonthArchive.as_view(),
        name="month_archive"
        ),
    url(r'page/(?P<page>[\d]$)', HomeView.as_view(), name='page'),
    url(r'^post/(?P<slug>[\w\d-]+)/$', PostDetail.as_view(), name='post'),
]
