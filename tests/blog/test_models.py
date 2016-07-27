"""Test for djangopress.blog.models."""
import pytest
from model_mommy import mommy

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from djangopress.blog.models import Post, Category


def test_post_str(mocker):
    """Test string representation for Post object."""
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category_mock.get_or_create.return_value = category, None
    post = mommy.prepare(Post)
    assert str(post) == 'No title'


def test_post_slug(mocker):
    """Test post slug is equal to post title slugified."""
    mocker.patch('django.db.models.Model.save', autospec=True)
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category_mock.get_or_create.return_value = category, None
    post = mommy.prepare(Post)
    post.title = 'A title'
    post.save()
    assert post.slug == slugify(post.title)


def test_post_custom_slug(mocker):
    """Test post slug is different than title."""
    mocker.patch('django.db.models.Model.save', autospec=True)
    post = mommy.prepare(Post)
    post.title = 'A title'
    post.slug = 'a-slug'
    post.save()
    assert post.slug != slugify(post.title)


def test_post_contains_slug():
    """Test post without slug raises exception."""
    post = mommy.prepare(Post)
    with pytest.raises(ValueError):
        post.save()


def test_post_absolute_url(mocker):
    """Test post's absolute url."""
    mocker.patch('django.db.models.Model.save', autospec=True)
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category_mock.get_or_create.return_value = category, None
    post = mommy.prepare(Post)
    post.title = 'A title'
    post.save()
    assert post.get_absolute_url == reverse("djangopress:post",
                                            kwargs={'slug': post.slug}
                                            )


def test_category_str():
    """Test string representation for Category object."""
    category = mommy.prepare(Category)
    assert str(category) == category.name
