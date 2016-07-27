from django.contrib import admin
from djangopress.blog.models import Post, Category
from djangopress.core.models import Option

admin.site.register(Option)
admin.site.register(Post)
admin.site.register(Category)
