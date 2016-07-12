"""Test djangopress templatetags."""
from django.template import Template, Context


def test_archive_list_tag():
    """Test the archive_list tag."""
    template_snippet = '{% load djangopress %}{% archive_list %}'
    Template(template_snippet).render(Context({}))
