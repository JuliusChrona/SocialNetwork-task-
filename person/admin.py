from django.contrib import admin

from person.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    pass
