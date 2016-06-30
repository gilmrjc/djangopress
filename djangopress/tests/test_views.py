"""Test djangopress views."""
try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

from model_mommy import mommy

from djangopress.views import HomeView
from djangopress.models import Post


def home_view_response(rf, mocker, posts=5):
    """Generate a HomeView response object."""
    option = mocker.patch('djangopress.views.Option.objects.get_or_create')
    option.return_value = Mock(), None
    posts_mock = mocker.patch('djangopress.models.Post.objects.all')
    posts_mock.return_value = mommy.prepare(Post, _quantity=posts)
    request = rf.get('/')
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
