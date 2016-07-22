"""Models for the comments app."""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.timezone import now

from djangopress.models import Post


@python_2_unicode_compatible
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

    def __str__(self):
        return '%s on %s' % (self.author, self.post)
