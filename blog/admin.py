from django.contrib import admin
from blog.models import Post, PostComment, PostImage, PostTag, Tag


class PostTagInline(admin.TabularInline):
    model = PostTag


class PostCommentInline(admin.TabularInline):
    model = PostComment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostTagInline,
        PostCommentInline
    ]


admin.site.register(Post, PostAdmin)
admin.site.register([PostComment, PostImage, PostTag, Tag])
