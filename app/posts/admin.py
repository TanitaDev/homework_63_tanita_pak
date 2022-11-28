from django.contrib import admin
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
