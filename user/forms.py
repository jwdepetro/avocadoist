from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User


class CustomUserCreationForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomerUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('email',)
