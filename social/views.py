from django.shortcuts import render
from social.models import UserProfile, SocialProfile


def index(request):
    """
    Show the user profile.
    :param request:
    :return:
    """
    user_profile = UserProfile.objects.first()
    social_profiles = SocialProfile.objects.all()

    return render(request, 'profile/index.html', {
        'user_profile': user_profile,
        'social_profiles': social_profiles
    })
