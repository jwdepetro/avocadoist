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
