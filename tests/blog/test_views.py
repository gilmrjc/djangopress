"""Test blog views."""
import random
try:
    from unittest.mock import Mock, PropertyMock
except ImportError:
    from mock import Mock, PropertyMock

from model_mommy import mommy

from django.utils.text import slugify
from django.core.urlresolvers import reverse

from djangopress.blog.views import PostList, PostDetail, MonthArchive
from djangopress.blog.models import Post, Category


def option_get_or_create_stub(number):
    """Stub the get_or_create for to be used by the method get_paginated_by."""
    def function_stub(name, defaults):
        """Mock the calling to get_or_create for Option"""
        mock = Mock()
        if name == 'posts_per_page':
            type(mock).value = PropertyMock(return_value=str(number))
        else:
            type(mock).value = PropertyMock(return_value=defaults['value'])
        return mock, None

    return function_stub


def general_options(mocker):
    """Generate the general options needed for the pages."""
    mocker.patch('djangopress.blog.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub(5)
                 )
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None


def post_list_response(rf, mocker, posts=5):
    """Generate a PostList response object."""
    general_options(mocker)
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=posts)
    request = rf.get(reverse('djangopress:home'))
    response = PostList.as_view()(request)
    return response


def test_post_list(rf, mocker):
    """Test PostList works."""
    response = post_list_response(rf, mocker)
    assert response.status_code == 200


def test_post_list_posts_in_context(rf, mocker):
    """Test Homeview context contains the posts."""
    response = post_list_response(rf, mocker)
    assert 'posts' in response.context_data


def test_post_list_pagination(rf, mocker):
    """Test Homeview paginates content."""
    response = post_list_response(rf, mocker)
    assert 'is_paginated' in response.context_data


def test_post_list_pagination_2_posts(rf, mocker):
    """Test PostList paginates content based on the number of posts."""
    response = post_list_response(rf, mocker, 2)
    assert not response.context_data['is_paginated']


def test_post_list_pagination_6_posts(rf, mocker):
    """Test PostList paginates content based on the number of posts."""
    response = post_list_response(rf, mocker, 6)
    assert response.context_data['is_paginated']


def test_post_list_custom_pagination(rf, mocker):
    """Test a custom pagination value."""
    general_options(mocker)
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=3)
    request = rf.get(reverse('djangopress:home'))
    response = PostList.as_view()(request)
    assert not response.context_data['is_paginated']


def test_post_list_custom_pagination_pag(rf, mocker):
    """Test a custom pagination value."""
    mocker.patch('djangopress.blog.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub('3')
                 )
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=4)
    request = rf.get(reverse('djangopress:home'))
    response = PostList.as_view()(request)
    assert response.context_data['is_paginated']


def test_post_list_pagination_pages(rf, mocker):
    """Test the pagination of the homepage."""
    general_options(mocker)
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=6)
    request = rf.get(reverse('djangopress:page', kwargs={'page': 2}))
    response = PostList.as_view()(request, page=2)
    assert response.context_data['page_obj'].number == 2


def test_bad_pagination_option(rf, mocker):
    """Test the behaviour when a bad pagination option is given."""
    mocker.patch('djangopress.blog.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub('a')
                 )
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=6)
    request = rf.get(reverse('djangopress:home'))
    response = PostList.as_view()(request)
    assert 'is_paginated' in response.context_data


def test_default_pagination_value(rf, mocker):
    """Test the default value when a bad pagination option is given."""
    mocker.patch('djangopress.blog.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub('a')
                 )
    category_mock = mocker.patch('djangopress.blog.models.Category.objects')
    category = mommy.prepare(Category, name='Uncategorized')
    category.pk = 1
    category_mock.get_or_create.return_value = category, None
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=6)
    request = rf.get(reverse('djangopress:home'))
    response = PostList.as_view()(request)
    assert response.context_data['paginator'].per_page == 5


def post_view_response(rf, mocker, posts=5):
    """Generate a PostDetail response object."""
    general_options(mocker)
    posts_list = mommy.prepare(Post, _quantity=posts)
    for post in posts_list:
        post.slug = slugify(post.title)
    post = random.choice(posts_list)
    get_object_mock = mocker.patch(
        'djangopress.blog.views.PostDetail.get_object'
        )
    get_object_mock.return_value = post
    request = rf.get(reverse('djangopress:post', kwargs={'slug': post.slug}))
    response = PostDetail.as_view()(request, slug=post.slug)
    return response


def test_post_view(rf, mocker):
    """Test PostDetail works."""
    response = post_view_response(rf, mocker)
    assert response.status_code == 200


def test_post_view_posts_in_context(rf, mocker):
    """Test PostDetail context contains the posts."""
    response = post_view_response(rf, mocker)
    assert 'post' in response.context_data


def month_archive_view_response(rf, mocker, posts=5):
    """Generate a PostDetail response object."""
    general_options(mocker)
    posts_mock = mocker.patch('djangopress.blog.models.Post.objects.all')
    posts_list = mommy.prepare(Post, _quantity=posts)
    posts_mock.return_value = posts_list
    mocker.patch('djangopress.blog.views.MonthArchive.get_ordering')
    mocker.patch('djangopress.blog.views.MonthArchive.get_dated_queryset')
    mocker.patch('djangopress.blog.views.MonthArchive.get_date_list')
    mocker.patch('django.views.generic.dates._get_next_prev')
    request = rf.get(reverse('djangopress:month_archive',
                             kwargs={'year': 2016, 'month': 5})
                     )
    response = MonthArchive.as_view()(request, year='2016', month='5')
    return response


def test_month_archive_view(rf, mocker):
    """Test the month archive view."""
    response = month_archive_view_response(rf, mocker)
    assert response.status_code == 200


def test_month_archive_posts_context(rf, mocker):
    """Test PostDetail context contains the posts."""
    response = month_archive_view_response(rf, mocker)
    assert 'posts' in response.context_data
