"""
Defines the views and routes for the social module.
"""

# pylint: disable-msg=E1101

from django.shortcuts import render
from social.models import UserProfile


def index(request):
    """
    Show the user profile.
    :param request:
    :return:
    """
    user_profile = UserProfile.objects.first()

    return render(request, 'profile/index.html', {'user_profile': user_profile})
