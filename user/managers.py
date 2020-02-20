"""
Defines the managers for the user module.
"""

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user manager where email is required and username is not.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a standard app user.
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        if not email:
            raise ValueError('email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a super user.
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser is not staff'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser is not a superuser'))
        return self.create_user(email, password, **extra_fields)
