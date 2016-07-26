"""Views for Djangopress Pages."""
from django.views.generic.detail import DetailView

from .models import Page


class PageDetail(DetailView):  # pylint: disable=too-many-ancestors
    """Page view."""
    model = Page
