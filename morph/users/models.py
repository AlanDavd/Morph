"""User related models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Default user for Morph.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={"unique": "A user with that email already exists."},
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    name = models.CharField("Name of User", blank=True, max_length=255)  # Little hack

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username.

        Returns:
            str: Username
        """
        return self.username
