"""Test for djangopress.core.models."""
from model_mommy import mommy

from djangopress.pages.models import Page


def test_page_str():
    """Test string representation for Page object."""
    page = mommy.prepare(Page)
    assert str(page) == page.title
