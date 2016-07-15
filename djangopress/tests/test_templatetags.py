"""Test djangopress templatetags."""
from random import randint
from datetime import date, timedelta

from model_mommy import mommy

from django.template import Template, Context

from djangopress.models import Post, Category
from djangopress.templatetags.djangopress_tags import archive_list
from djangopress.templatetags.djangopress_tags import category_list


def random_date(start, end):
    """Generate a random date between the limits."""
    days = int((end - start).days)
    random_delta = timedelta(days=randint(0, days))
    return start + random_delta


def test_archive_list_tag(mocker):
    """Test the archive_list tag."""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts = mommy.prepare(Post, _quantity=20)
    posts_mock.return_value = posts
    template_snippet = '{% load djangopress_tags %}{% archive_list %}'
    Template(template_snippet).render(Context({}))


def test_archive_list_dictionary(mocker):
    """Test the dictionary of archive list."""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts = mommy.prepare(Post, _quantity=20)
    posts_mock.return_value = posts
    assert isinstance(archive_list(), dict)


def test_archive_list_posts(mocker):
    """Test the dictionary with the months and years."""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts = mommy.prepare(Post, _quantity=20)
    dates = ([date(2016, 2, 1), date(2016, 2, 20)],
             [date(2016, 2, 1), date(2016, 2, 20)],
             [date(2016, 2, 1), date(2016, 2, 20)],
             [date(2016, 2, 1), date(2016, 2, 20)],
             [date(2016, 3, 1), date(2016, 3, 20)],
             [date(2016, 3, 1), date(2016, 3, 20)],
             [date(2016, 4, 1), date(2016, 4, 20)],
             [date(2016, 4, 1), date(2016, 4, 20)],
             [date(2016, 4, 1), date(2016, 4, 20)],
             [date(2016, 4, 1), date(2016, 4, 20)],
             [date(2016, 5, 1), date(2016, 5, 20)],
             [date(2016, 6, 1), date(2016, 6, 20)],
             [date(2016, 6, 1), date(2016, 6, 20)],
             [date(2016, 7, 1), date(2016, 7, 20)],
             [date(2016, 8, 1), date(2016, 8, 20)],
             [date(2016, 8, 1), date(2016, 8, 20)],
             [date(2016, 8, 1), date(2016, 8, 20)],
             [date(2016, 9, 1), date(2016, 9, 20)],
             [date(2016, 9, 1), date(2016, 9, 20)],
             [date(2016, 9, 1), date(2016, 9, 20)],
             )
    for i, post in enumerate(posts):
        post.creation_date = random_date(dates[i][0], dates[i][1])
    posts_mock.return_value = posts
    dictionary = {}
    dates_dictionary = {}
    dates_dictionary['2016'] = []
    dates_dictionary['2016'].append(date(2016, 2, 1))
    dates_dictionary['2016'].append(date(2016, 3, 1))
    dates_dictionary['2016'].append(date(2016, 4, 1))
    dates_dictionary['2016'].append(date(2016, 5, 1))
    dates_dictionary['2016'].append(date(2016, 6, 1))
    dates_dictionary['2016'].append(date(2016, 7, 1))
    dates_dictionary['2016'].append(date(2016, 8, 1))
    dates_dictionary['2016'].append(date(2016, 9, 1))
    dictionary['years'] = dates_dictionary
    assert archive_list() == dictionary


def test_category_list_tag(mocker):
    """Test category list templatetag"""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts = mommy.prepare(Post, _quantity=20)
    posts_mock.return_value = posts
    template_snippet = '{% load djangopress_tags %}{% category_list %}'
    Template(template_snippet).render(Context({}))


def test_category_list_dictionary(mocker):
    """Test the dictionary of archive list."""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts = mommy.prepare(Post, _quantity=20)
    posts_mock.return_value = posts
    assert isinstance(category_list(), dict)


def test_category_list_content(mocker):
    """Test the dictionary with the months and years."""
    category_mock = mocker.patch('djangopress.models.Category.objects')
    uncategorized = mommy.prepare(Category, name='Uncategorized')
    uncategorized.pk = 1
    categories = mommy.prepare(Category, _quantity=3)
    categories.insert(0, uncategorized)
    category_mock.all.return_value = categories
    dictionary = {}
    dictionary['categories'] = categories
    assert category_list() == dictionary
