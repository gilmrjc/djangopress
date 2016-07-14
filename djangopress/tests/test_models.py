"""Test for djangopress models."""
import pytest
from model_mommy import mommy

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from djangopress.models import Post, Option, Category


def test_post_str(mocker):
    """Test string representation for Post object."""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category_mock.get_or_create.return_value = category, None
    post = mommy.prepare(Post)
    assert str(post) == post.title


def test_post_slug(mocker):
    """Test post slug is equal to post titlepost title slugified."""
    save = mocker.patch('django.db.models.Model.save', autospec=True)
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category_mock.get_or_create.return_value = category, None
    post = mommy.make(Post)
    save.assert_called_with(post)
    assert post.slug == slugify(post.title)


def test_post_absolute_url(mocker):
    """Test post's absolute url."""
    mocker.patch('django.db.models.Model.save', autospec=True)
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category_mock.get_or_create.return_value = category, None
    post = mommy.make(Post)
    assert post.get_absolute_url == reverse("djangopress:post",
                                            kwargs={'slug': post.slug}
                                            )


def test_option_str():
    """Test string representation for Option object."""
    option = mommy.prepare(Option)
    assert str(option) == option.name


def test_category_str():
    """Test string representation for Category object."""
    category = mommy.prepare(Category)
    assert str(category) == category.name


@pytest.mark.django_db
def test_default_category(mocker):
    """Test default category is 'Uncategorized'."""
    # mocker.patch('django.db.models.Model.save', autospec=True)
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.make(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    post = mommy.make(Post)
    assert post.category == category
