"""
Defines all custom admin settings for the blog module.
"""

from django.contrib import admin
from blog.models import Post, PostComment, PostImage, PostTag, Tag


class PostTagInline(admin.TabularInline):
    """
    Post tag
    """
    model = PostTag


class PostCommentInline(admin.TabularInline):
    """
    Post comment
    """
    model = PostComment


class PostImageInline(admin.TabularInline):
    """
    Post image
    """
    model = PostImage


class TagAdmin(admin.ModelAdmin):
    """
    Tag admin
    """
    list_display = ('name', 'post_count')
    list_filter = ('name',)
    search_fields = ('name',)


class PostCommentAdmin(admin.ModelAdmin):
    """
    Post comment admin
    """
    list_display = ('post_title', 'name', 'comment', 'is_user_blocked', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'created_at')


class PostImageAdmin(admin.ModelAdmin):
    """
    Post image admin
    """
    list_display = ('post_title', 'image_name')


class PostTagAdmin(admin.ModelAdmin):
    """
    Post tag admin
    """
    list_display = ('post_title', 'tag_name')


class PostAdmin(admin.ModelAdmin):
    """
    Post admin

    This is the most commonly used admin interface
    """
    list_display = ('title', 'slug', 'image_count', 'comment_count', 'tags', 'created_at')
    list_filter = ('title', 'slug', 'created_at')
    search_fields = ('title', 'slug', 'created_at')
    inlines = [
        PostImageInline,
        PostTagInline,
        PostCommentInline
    ]


admin.site.register(Tag, TagAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostImage, PostImageAdmin)
admin.site.register(PostTag, PostTagAdmin)
admin.site.register(Post, PostAdmin)
