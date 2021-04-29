"""User admin config."""

# Django
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Admin user model."""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('username',)


admin.site.register(User, CustomUserAdmin)
