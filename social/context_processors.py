"""
Context processors for the social module.
"""

# pylint: disable-msg=E1101
# pylint: disable-msg=W0613

from social.models import SocialProfile


def social_profiles(request):
    """
    Always return all social profiles for various views and links.

    :param request:
    :return:
    """
    return {
        'social_profiles': SocialProfile.objects.all()
    }
