"""
Defines all storage classes used to manage assets.
"""

# pylint: disable-msg=W0223

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Static storage definition.
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Media storage definition.
    """
    location = settings.MEDIAFILES_LOCATION
