"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

# GENERAL
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="M7eE41HDgLLgmM3QUV2DAc5tPjtSNa8XgcPdCLLooVfg5GKiLbbjmN7nfRvZuoZc",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]
