"""Test djangopress views."""
from unittest.mock import Mock

from djangopress.views import HomeView


def test_home_view(rf, mocker):
    """Test HomeView works"""
    option = mocker.patch('djangopress.views.Option.objects.get_or_create')
    option.return_value = (Mock(), None)
    mocker.patch('djangopress.models.Post.objects.all')
    request = rf.get('/')
    response = HomeView.as_view()(request)
    assert response.status_code == 200


def test_home_view_context(rf, mocker):
    """Test Homeview context"""
    option = mocker.patch('djangopress.views.Option.objects.get_or_create')
    option.return_value = (Mock(), None)
    post = mocker.patch('djangopress.models.Post.objects.all')
    request = rf.get('/')
    response = HomeView.as_view()(request)
    assert option.called
    assert post.called
    assert 'title' in response.context_data
    assert 'tagline' in response.context_data
    assert 'posts' in response.context_data
