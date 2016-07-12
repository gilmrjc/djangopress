"""Test djangopress templatetags."""
from django.template import Template, Context

from djangopress.templatetags.djangopress import archive_list


def test_archive_list_tag():
    """Test the archive_list tag."""
    template_snippet = '{% load djangopress %}{% archive_list %}'
    Template(template_snippet).render(Context({}))


def test_archive_list_dictionary():
    """Test the dictionary of archive list."""
    dictionary = archive_list()
    assert dictionary == {}
