"""Test for djangopress models."""
import pytest
from model_mommy import mommy

from django.template.defaultfilters import slugify
from djangopress.models import Post, Option


def test_post_str():
    """Test string representation for Post object"""
    post = mommy.prepare(Post)
    assert str(post) == post.title


@pytest.mark.django_db
def test_post_slug():
    """Test post slug is equal to post titlepost title slugified"""
    post = mommy.make(Post)
    assert post.slug == slugify(post.title)


def test_option_str():
    """Test string representation for Option object"""
    option = mommy.prepare(Option)
    assert str(option) == option.name
