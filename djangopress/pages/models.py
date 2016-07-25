"""Page models."""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Page(models.Model):
    """Page model."""
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        """String representation of Page."""
        return self.title
