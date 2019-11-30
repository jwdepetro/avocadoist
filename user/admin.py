from django.contrib import admin
from user.models import User, AnonymousUser

admin.site.register([User, AnonymousUser])
