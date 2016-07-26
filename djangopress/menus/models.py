"""Models for menu app."""
from __future__ import unicode_literals
import re
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse, NoReverseMatch


@python_2_unicode_compatible
class Menu(models.Model):
    """Menu model."""
    name = models.CharField(max_length=255)

    def __str__(self):
        """String representation of Menu."""
        return self.name


@python_2_unicode_compatible
class MenuItem(models.Model):
    """MenuItem model."""
    menu = models.ForeignKey('Menu',
                             on_delete=models.CASCADE,
                             related_name='items',
                             )
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='subitems',
                               blank=True,
                               null=True,
                               )
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=255,
                              blank=True,
                              null=True
                              )
    separator = models.BooleanField(default=False)

    def __str__(self):
        """String representation of MenuItem."""
        return self.name

    def get_absolute_url(self):
        """Get the absolute url of MenuItem target."""
        try:
            target, *args = re.split(';', self.target)
            kwargs = {}
            for arg in args:
                key, value = re.split('=', arg)
                kwargs[key] = value
            url = reverse(target, kwargs=kwargs)
        except NoReverseMatch:
            url = self.target or '#'
        return url
