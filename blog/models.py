from django.db import models
from media.models import Image
from user.models import User, AnonymousUser
from app.models import AbstractBaseModel
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Tag(AbstractBaseModel):
    """
    Tag for categorizing posts
    """
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        db_table = 'blog_tag'

    def __str__(self):
        return self.name


class Post(AbstractBaseModel):
    """
    Blog post
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=250)
    body = models.TextField(_('body'))
    meta_title = models.CharField(_('meta title'), max_length=250, null=True)
    meta_description = models.CharField(_('meta description'), max_length=1000, null=True)

    # Override the default created_at to make this editable
    created_at = models.DateTimeField(_('created at'), default=timezone.now)

    class Meta:
        db_table = 'blog_post'

    def __str__(self):
        return self.title


class PostComment(AbstractBaseModel):
    """
    Blog post comment
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    anonymous_user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)
    comment = models.CharField(_('comment'), max_length=250)

    class Meta:
        db_table = 'blog_post_comment'

    def __str__(self):
        return self.comment


class PostImage(AbstractBaseModel):
    """
    Blog post image
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_post_image'


class PostTag(AbstractBaseModel):
    """
    Blog post tag
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_post_tag'

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.tag.name)
