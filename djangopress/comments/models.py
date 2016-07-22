"""Models for the comments app."""
from django.db import models
from django.utils.timezone import now

from djangopress.models import Post


class Comment(models.Model):
    """Comment model."""
    content = models.TextField()
    author = models.CharField(max_length=255)
    author_email = models.EmailField()
    author_website = models.URLField(blank=True, null=True)
    creation_date = models.DateTimeField(default=now)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE
                             )
