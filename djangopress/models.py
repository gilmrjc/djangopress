"""Djangopress models."""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Post(models.Model):
    """Post Model."""

    STATUS_CHOICES = (('D', 'Draft'),
                      ('PB', 'Public'),
                      ('PV', 'Private'),
                      ('T', 'Trash'),
                      )

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE
                               )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, default=now)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    modified_date = models.DateTimeField(editable=False)
    content_filtered = models.TextField()
    parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)

    @property
    def get_absolute_url(self):
        """Get the absolute url of a post"""
        return reverse('djangopress:post', kwargs={'slug': self.slug})

    def __str__(self):
        """String representation of Post object"""
        return self.title

    def save(self, *args, **kwargs):
        """Save the Post object and create a slug"""
        self.slug = slugify(self.title)
        self.modified_date = now()
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-creation_date']


# class CommentMeta(models.Model):
#     """Meta information of comments."""
#     comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
#     key = models.CharField(max_length=255)
#     value = models.TextField(blank=True, null=True)
#
#
# class Comment(models.Model):
#     """Comment."""
#     post = models.ForeignKey(Post, models.CASCADE)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                on_delete=models.CASCADE
#                                )
#     creation_date = models.DateTimeField()
#     content = models.TextField()
#     comment_karma = models.IntegerField()
#     approved = models.CharField(max_length=20)
#     agent = models.CharField(max_length=255)
#     comment_type = models.CharField(max_length=20)
#     parent = models.ForeignKey('Comment')
#
#
# class Link(models.Model):
#     """Link."""
#     link_url = models.CharField(max_length=255)
#     link_name = models.CharField(max_length=255)
#     link_image = models.CharField(max_length=255)
#     link_target = models.CharField(max_length=25)
#     link_description = models.CharField(max_length=255)
#     link_visible = models.CharField(max_length=20)
#     link_owner = models.BigIntegerField()
#     link_rating = models.IntegerField()
#     link_updated = models.DateTimeField()
#     link_rel = models.CharField(max_length=255)
#     link_notes = models.TextField()
#     link_rss = models.CharField(max_length=255)
#
#
@python_2_unicode_compatible
class Option(models.Model):
    """Option."""
    name = models.CharField(unique=True, max_length=191)
    value = models.CharField(max_length=255)

    def __str__(self):
        """String representation of Option object"""
        return self.name


# class PostMeta(models.Model):
#     """Meta information about posts."""
#     post = models.ForeignKey('Post')
#     key = models.CharField(max_length=255)
#     value = models.TextField(blank=True, null=True)
#
#
# class TermRelationship(models.Model):
#     """Terms."""
#     object_id = models.BigIntegerField()
#     term_taxonomy_id = models.BigIntegerField()
#     term_order = models.IntegerField()
#
#     class Meta:
#         unique_together = (('object_id', 'term_taxonomy_id'),)
#
#
# class TermTaxonomy(models.Model):
#     """Term taxonomy."""
#     term_taxonomy_id = models.BigIntegerField(primary_key=True)
#     term_id = models.BigIntegerField()
#     taxonomy = models.CharField(max_length=32)
#     description = models.TextField()
#     parent = models.BigIntegerField()
#     count = models.BigIntegerField()
#
#     class Meta:
#         unique_together = (('term_id', 'taxonomy'),)
#
#
# class TermMeta(models.Model):
#     """Meta term."""
#     meta_id = models.BigIntegerField(primary_key=True)
#     term_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=255, blank=True, null=True)
#     meta_value = models.TextField(blank=True, null=True)
#
#
# class Term(models.Model):
#     """Term."""
#     term_id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     slug = models.CharField(max_length=200)
#     term_group = models.BigIntegerField()
#
#
# class UserMeta(models.Model):
#     "UserMeta information."""
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE
#                              )
#     meta_key = models.CharField(max_length=255, blank=True, null=True)
#     meta_value = models.TextField(blank=True, null=True)
