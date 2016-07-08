"""Test djangopress views."""
try:
    from unittest.mock import Mock, PropertyMock
except ImportError:
    from mock import Mock, PropertyMock

from model_mommy import mommy

from django.core.urlresolvers import reverse

from djangopress.views import HomeView
from djangopress.models import Post


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


def home_view_response(rf, mocker, posts=5):
    """Generate a HomeView response object."""
    mocker.patch('djangopress.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub(5)
                 )
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=posts)
    request = rf.get(reverse('djangopress:home'))
    response = HomeView.as_view()(request)
    return response


def test_home_view(rf, mocker):
    """Test HomeView works."""
    response = home_view_response(rf, mocker)
    assert response.status_code == 200


def test_home_view_title_in_context(rf, mocker):
    """Test Homeview context containts the title."""
    response = home_view_response(rf, mocker)
    assert 'title' in response.context_data


def test_home_view_tagline_in_context(rf, mocker):
    """Test Homeview context contains the tagline."""
    response = home_view_response(rf, mocker)
    assert 'tagline' in response.context_data


def test_home_view_posts_in_context(rf, mocker):
    """Test Homeview context contains the posts."""
    response = home_view_response(rf, mocker)
    assert 'posts' in response.context_data


def test_home_page_pagination(rf, mocker):
    """Test Homeview paginates content."""
    response = home_view_response(rf, mocker)
    assert 'is_paginated' in response.context_data


def test_home_view_pagination_2_posts(rf, mocker):
    """Test HomeView paginates content based on the number of posts."""
    response = home_view_response(rf, mocker, 2)
    assert not response.context_data['is_paginated']


def test_home_view_pagination_6_posts(rf, mocker):
    """Test HomeView paginates content based on the number of posts."""
    response = home_view_response(rf, mocker, 6)
    assert response.context_data['is_paginated']


def test_home_view_custom_pagination(rf, mocker):
    """Test a custom pagination value."""
    mocker.patch('djangopress.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub(3)
                 )
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=3)
    request = rf.get(reverse('djangopress:home'))
    response = HomeView.as_view()(request)
    assert not response.context_data['is_paginated']


def test_home_view_custom_pagination_pag(rf, mocker):
    """Test a custom pagination value."""
    mocker.patch('djangopress.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub(3)
                 )
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=4)
    request = rf.get(reverse('djangopress:home'))
    response = HomeView.as_view()(request)
    assert response.context_data['is_paginated']


def test_home_view_pagination_pages(rf, mocker):
    """Test the pagination of the homepage."""
    mocker.patch('djangopress.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub(5)
                 )
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=6)
    request = rf.get(reverse('djangopress:page', kwargs={'page': 2}))
    response = HomeView.as_view()(request, page=2)
    assert response.context_data['page_obj'].number == 2


def test_bad_pagination_option(rf, mocker):
    """Test the behaviour when a bad pagination option is given."""
    mocker.patch('djangopress.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub('a')
                 )
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=6)
    request = rf.get(reverse('djangopress:home'))
    response = HomeView.as_view()(request)
    assert 'is_paginated' in response.context_data


def test_default_pagination_value(rf, mocker):
    """Test the default value when a bad pagination option is given."""
    mocker.patch('djangopress.views.Option.objects.get_or_create',
                 new=option_get_or_create_stub('a')
                 )
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=6)
    request = rf.get(reverse('djangopress:home'))
    response = HomeView.as_view()(request)
    assert response.context_data['paginator'].per_page == 5
