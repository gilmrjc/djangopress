"""Templatetags for comments app."""
from django.template import Library

from ..models import Comment

register = Library()


@register.inclusion_tag('comments/tags/comments_list.html')
def show_comments(post):
    """Show the comments of the current post."""
    return {'comments': post.comment_set.all()}


@register.inclusion_tag('comments/tags/recent_comments.html')
def recent_comments():
    """Show the most recent comments in the blog."""
    comments = Comment.objects.all().order_by('-creation_date')[:5]
    return {'comments': comments}
