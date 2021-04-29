"""Picture Celery tasks."""

# Django
from django.contrib.auth import get_user_model

# Celery
from config import celery_app

# Models
from morph.pictures.models import Post
User = get_user_model()


@celery_app.task(name="bulk_image_uploading")
def bulk_image_uploading(user, title, images):
    """Save one or more images to store."""
    for file in images.getlist("image"):
        instance = Post(
            owner=User.objects.get(pk=user),
            title=title,
            image=file,
        )
        instance.save()
