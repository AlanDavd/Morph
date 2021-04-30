"""Pictures app config."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PicturesConfig(AppConfig):
    """Pictures app."""

    name = "morph.pictures"
    verbose_name = _("Pictures")

    def ready(self):
        try:
            import morph.pictures.signals  # noqa F401
        except ImportError:
            pass
