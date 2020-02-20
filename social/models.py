"""
Defines all models for the social module.
"""

# pylint: disable-msg=R0903

from django.db import models
from django.utils.translation import ugettext_lazy as _
from djrichtextfield.models import RichTextField

from app.models import AbstractBaseModel
from media.models import Image


class SocialType(AbstractBaseModel):
    """
    Social type

    Examples are facebook, instagram, etc.
    """
    name = models.CharField(_('name'), max_length=100)
    icon = models.CharField(_('icon'), max_length=100)

    class Meta:
        """
        Override the table name.
        """
        db_table = 'social_social_type'

    def __str__(self):
        return self.name


class SocialProfile(AbstractBaseModel):
    """
    Social profile

    Maps a URL to a specific social type.
    """
    social_type = models.ForeignKey(SocialType, on_delete=models.CASCADE, related_name='social')
    name = models.CharField(_('name'), max_length=100)
    link = models.URLField(_('link'))
    weight = models.IntegerField(_('weight'))

    class Meta:
        """
        Override the table name.
        """
        db_table = 'social_social_profile'

    def __str__(self):
        return self.name


class UserProfile(AbstractBaseModel):
    """
    User profile

    Public profile in the app that users can view.
    """
    title = models.CharField(_('title'), max_length=250)
    body = RichTextField(_('about me'))
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        """
        Override the table name.
        """
        db_table = 'social_user_profile'

    def __str__(self):
        return self.title
