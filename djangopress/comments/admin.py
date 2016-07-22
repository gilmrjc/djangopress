"""Admin models for comments."""
from django.contrib import admin

from .models import Comment


admin.site.register(Comment)
