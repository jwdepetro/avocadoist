"""
Defines the models for the user module.
"""

# pylint: disable-msg=R0903

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.models import AbstractBaseModel
from user.managers import UserManager


class User(AbstractUser):
    """
    Overrides the default Django user model.
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        """
        Override the table name.
        """
        db_table = 'user_user'

    def __str__(self):
        return self.email


class AnonymousUser(AbstractBaseModel):
    """
    Anonymous user can view and comment on posts as long as they are not blocked.
    """
    identifier = models.CharField(_('anonymous identifier'), unique=True, max_length=1000)
    ip_address = models.GenericIPAddressField(_('ip address'))
    is_blocked = models.BooleanField(_('is blocked'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        """
        Override the table name.
        """
        db_table = 'user_anonymous_user'

    def __str__(self):
        return self.identifier
