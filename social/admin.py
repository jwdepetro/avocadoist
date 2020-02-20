"""
Defines all custom admin settings for the social module.
"""

from django.contrib import admin
from social.models import SocialType, SocialProfile, UserProfile

admin.site.register([SocialType, SocialProfile, UserProfile])
