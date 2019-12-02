from django.contrib import admin
from blog.models import Post, PostComment, PostImage, PostTag, Tag


class PostTagInline(admin.TabularInline):
    model = PostTag


class PostCommentInline(admin.TabularInline):
    model = PostComment


class PostImageInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
        PostTagInline,
        PostCommentInline
    ]


admin.site.register(Post, PostAdmin)
admin.site.register([PostComment, PostImage, PostTag, Tag])
