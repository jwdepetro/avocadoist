from django.db import models
from django.utils.translation import ugettext_lazy as _
from djrichtextfield.models import RichTextField
from app.models import AbstractBaseModel
from media.models import Image


class SocialType(AbstractBaseModel):
    name = models.CharField(_('name'), max_length=100)
    icon = models.CharField(_('icon'), max_length=100)

    class Meta:
        db_table = 'social_social_type'

    def __str__(self):
        return self.name


class SocialProfile(AbstractBaseModel):
    social_type = models.ForeignKey(SocialType, on_delete=models.CASCADE, related_name='social')
    name = models.CharField(_('name'), max_length=100)
    link = models.URLField(_('link'))
    weight = models.IntegerField(_('weight'))

    class Meta:
        db_table = 'social_social_profile'

    def __str__(self):
        return self.name


class UserProfile(AbstractBaseModel):
    title = models.CharField(_('title'), max_length=250)
    body = RichTextField(_('about me'))
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        db_table = 'social_user_profile'

    def __str__(self):
        return self.title
