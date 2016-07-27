from django.contrib import admin

from djangopress.comments.models import Comment
from djangopress.menus.models import Menu, MenuItem
from djangopress.pages.models import Page
from djangopress.blog.models import Post, Category
from djangopress.core.models import Option

admin.site.register(Comment)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Page)
admin.site.register(Option)
admin.site.register(Post)
admin.site.register(Category)
