"""
Defines the forms for the user module.
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User


class CustomUserCreationForm(UserChangeForm):
    """
    Custom create user form
    """
    class Meta(UserCreationForm):
        """
        Override the model and fields
        """
        model = User
        fields = ('email',)


class CustomerUserChangeForm(UserChangeForm):
    """
    Custom edit user form
    """
    class Meta(UserChangeForm):
        """
        Override the model and fields
        """
        model = User
        fields = ('email',)
