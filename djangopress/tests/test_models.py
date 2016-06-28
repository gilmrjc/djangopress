"""Test for djangopress models."""
from model_mommy import mommy

from django.template.defaultfilters import slugify
from djangopress.models import Post, Option


def test_post_str():
    """Test string representation for Post object"""
    post = mommy.prepare(Post)
    assert str(post) == post.title


def test_post_slug(mocker):
    """Test post slug is equal to post titlepost title slugified"""
    mocker.patch('django.db.models.Model.save', autospec=True)
    post = mommy.make(Post)
    assert post.slug == slugify(post.title)


def test_option_str():
    """Test string representation for Option object"""
    option = mommy.prepare(Option)
    assert str(option) == option.name
