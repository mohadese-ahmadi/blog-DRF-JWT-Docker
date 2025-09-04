from django.contrib import admin
from .models import Blogs, Category, Tags, Comment, MenuItem
# Register your models here.


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "order", "parent")
    list_editable = ("url", "order", "parent")
