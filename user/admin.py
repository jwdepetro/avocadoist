from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User, AnonymousUser
from user.forms import CustomUserCreationForm, CustomerUserChangeForm
from django.utils.translation import ugettext_lazy as _


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomerUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_staff'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


class AnonymousUserAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'ip_address', 'is_blocked', 'created_at')
    list_filter = ('identifier', 'ip_address', 'is_blocked', 'created_at')
    search_fields = ('identifier', 'ip_address')


admin.site.register(User, UserAdmin)
admin.site.register(AnonymousUser, AnonymousUserAdmin)
