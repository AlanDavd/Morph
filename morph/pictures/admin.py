"""Posts model."""

# Django
from django.contrib import admin

# Models
from morph.pictures.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ("id", "owner", "title", "image")
    search_fields = ("title", "owner__username", "owner__email")
    list_filter = ("created", "modified")
