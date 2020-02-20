"""
Defines all generic base models across the entire app.
"""

# pylint: disable-msg=R0903

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractBaseModel(models.Model):
    """
    Abstract base model to be inherited by all models.
    """
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        """
        Define the model as abstract to avoid migrations.
        """
        abstract = True
