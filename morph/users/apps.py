"""User app config."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """User app."""
    name = "morph.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import morph.users.signals  # noqa F401
        except ImportError:
            pass
