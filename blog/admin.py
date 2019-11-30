from django.contrib import admin
from blog.models import Post, PostComment, PostImage, PostTag, Tag

admin.site.register([Post, PostComment, PostImage, PostTag, Tag])
