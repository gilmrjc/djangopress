"""Views for Djangopress Pages."""
from django.views.generic.detail import DetailView

from djangopress.views import DjangoPressMixin
from .models import Page


class PageDetail(DjangoPressMixin,  # pylint: disable=too-many-ancestors
                 DetailView):
    """Page view."""
    model = Page
