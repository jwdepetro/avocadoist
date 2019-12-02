from django.contrib import admin
from social.models import SocialType, SocialProfile, UserProfile

admin.site.register([SocialType, SocialProfile, UserProfile])
