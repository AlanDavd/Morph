"""User Celery tasks."""

# Django
from django.contrib.auth import get_user_model

# Celery
from config import celery_app

# Set up
User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()
