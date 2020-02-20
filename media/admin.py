"""
Defines all custom admin settings for the media module.
"""

from django.contrib import admin
from media.models import Image


class ImageAdmin(admin.ModelAdmin):
    """
    Image admin
    """
    list_display = ('name', 'meta_title', 'meta_description', 'created_at')
    list_filter = ('name', 'meta_title', 'meta_description', 'created_at')
    search_fields = ('name', 'meta_title', 'meta_description', 'created_at')


admin.site.register(Image, ImageAdmin)
