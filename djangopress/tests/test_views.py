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
    def get_or_create_util(name, **kwargs):
        """Util function for get_or_create mock."""
        if name == 'posts_per_page':
            return '5', None
        return Mock(), None
    options = mocker.patch('djangopress.views.Option.objects.get_or_create')
    options.side_effect = get_or_create_util
    posts_mock = mocker.patch('djangopress.views.Post.objects.all')
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


def test_home_no_pagination(rf, mocker):
    """Test HomeView uses no pagination when displaying 5 posts."""
    response = home_view_response(rf, mocker)
    assert not response.context_data['page_obj'].has_previous()
    assert not response.context_data['page_obj'].has_next()


def test_home_pagination(rf, mocker):
    """Test HomeView uses pagination when displaying 15 posts."""
    response = home_view_response(rf, mocker, posts=15)
    assert response.context_data['page_obj'].has_previous
    assert response.context_data['page_obj'].has_next
