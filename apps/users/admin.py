from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    list_filter = ['is_staff', 'is_active']

    fieldsets = (
        (_('Main Info'), {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name', 'preferred_name', 'phone_number', 'profile_picture')
        }),
        (_('Important Dates'), {
            'fields': ('last_login', 'date_joined')
        }),
        (_('Password Reset'), {
            'fields': ('reset_password_code',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    readonly_fields = ['email', 'last_login', 'date_joined', 'reset_password_code']

    search_fields = ['email', 'first_name', 'last_name']
    def has_add_permission(self, request, obj=None):
        return False


