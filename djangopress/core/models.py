"""Djangopress models."""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Option(models.Model):
    """Option."""
    name = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        """String representation of Option object"""
        return self.name
