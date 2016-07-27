"""Test comments templatetags."""
from model_mommy import mommy

from django.template import Template, Context

from djangopress.blog.models import Post
from djangopress.comments.templatetags.comments_tags import show_comments


def test_show_comments_tag(mocker):
    """Test the archive_list tag."""
    post = mommy.prepare(Post)
    post.comment_set.all = []
    template_snippet = '{% load comments_tags %}{% show_comments post %}'
    Template(template_snippet).render(Context({'post': post}))


def test_show_comments_content(mocker):
    """Test show comments content."""
    comments = mocker.patch('djangopress.blog.models.Post.comment_set')
    post = mommy.prepare(Post)
    post.pk = 1
    show_comments(post)
    comments.all.assert_called_once_with()
