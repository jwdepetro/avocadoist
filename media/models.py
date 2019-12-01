from django.db import models
from django.utils.translation import ugettext_lazy as _
from app.models import AbstractBaseModel


class Image(AbstractBaseModel):
    """
    A image hosted on S3
    """
    name = models.CharField(_('asset name'), max_length=250)
    meta_title = models.CharField(_('meta title'), max_length=250, null=True)
    meta_description = models.CharField(_('meta description'), max_length=1000, null=True)
    image = models.FileField()

    class Meta:
        db_table = 'media_image'

    def __str__(self):
        return self.name
