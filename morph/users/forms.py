"""User forms."""

# Django
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Auth set up
User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    """User change form updates user's fields."""

    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    """User creation form.
    Basic user model creation.
    """
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
