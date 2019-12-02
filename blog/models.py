from django.db import models
from media.models import Image
from user.models import AnonymousUser
from app.models import AbstractBaseModel
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from djrichtextfield.models import RichTextField


class Tag(AbstractBaseModel):
    """
    Tag for categorizing posts
    """
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        db_table = 'blog_tag'

    def __str__(self):
        return self.name

    def post_count(self):
        return self.post_tags.count()


class Post(AbstractBaseModel):
    """
    Blog post
    """
    title = models.CharField(_('title'), max_length=250)
    slug = models.CharField(_('slug'), max_length=250, unique=True)
    body = RichTextField(_('body'))
    meta_title = models.CharField(_('meta title'), max_length=250, null=True)
    meta_description = models.CharField(_('meta description'), max_length=1000, null=True)

    # Override the default created_at to make this editable
    created_at = models.DateTimeField(_('created at'), default=timezone.now)

    def comment_count(self):
        return self.post_comments.count()

    def image_count(self):
        return self.post_images.count()

    def tags(self):
        tags = []
        for post_tag in self.post_tags.all():
            tags.append(post_tag.tag.name)
        return ', '.join(sorted(tags))

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
    name = models.CharField(_('name'), max_length=30)
    comment = models.CharField(_('comment'), max_length=250)

    def post_title(self):
        return self.post.title

    def is_user_blocked(self):
        return self.anonymous_user.is_blocked

    class Meta:
        db_table = 'blog_post_comment'
        ordering = ['-created_at']

    def __str__(self):
        return self.comment


class PostImage(AbstractBaseModel):
    """
    Blog post image
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='post_images')

    def post_title(self):
        return self.post.title

    def image_name(self):
        return self.image.name

    class Meta:
        db_table = 'blog_post_image'

    def __str__(self):
        return self.image.name


class PostTag(AbstractBaseModel):
    """
    Blog post tag
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post_tags')

    def post_title(self):
        return self.post.title

    def tag_name(self):
        return self.tag.name

    class Meta:
        db_table = 'blog_post_tag'

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.tag.name)
