from django.contrib import admin
from djangopress.models import Post, Option, UserMeta

admin.site.register(UserMeta)
admin.site.register(Option)
admin.site.register(Post)
