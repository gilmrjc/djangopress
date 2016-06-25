"""Djangopress models."""
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Post(models.Model):
    """Post Model."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    excerpt = models.TextField()
    creation_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    modified_date = models.DateTimeField()
    content_filtered = models.TextField()
    parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)


class CommentMeta(models.Model):
    """Meta information of comments."""
    comment = models.ForeignKey('Comment', models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)


class Comment(models.Model):
    """Comment."""
    post = models.ForeignKey(Post, models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    creation_date = models.DateTimeField()
    content = models.TextField()
    comment_karma = models.IntegerField()
    approved = models.CharField(max_length=20)
    agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    parent = models.ForeignKey('Comment')


class Link(models.Model):
    """Link."""
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)


class Option(models.Model):
    """Option."""
    name = models.CharField(unique=True, max_length=191)
    value = models.TextField()
    autoload = models.CharField(max_length=20)


class PostMeta(models.Model):
    """Meta information about posts."""
    post = models.ForeignKey('Post')
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)


class TermRelationship(models.Model):
    """Terms."""
    object_id = models.BigIntegerField()
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        unique_together = (('object_id', 'term_taxonomy_id'),)


class TermTaxonomy(models.Model):
    """Term taxonomy."""
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        unique_together = (('term_id', 'taxonomy'),)


class TermMeta(models.Model):
    """Meta term."""
    meta_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)


class Term(models.Model):
    """Term."""
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()


class UserMeta(models.Model):
    "UserMeta information."""
    umeta_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)
