"""Pictures relates models."""

# Django
from django.db import models


class Post(models.Model):
    """Post model holds basic data for this example.
    Post models acts as a container for an image.
    Every picture is stored in a repository, that repository
    is the user's profile.
    """

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="users/pictures")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username of model representation."""
        return f"{self.title} by @{self.owner.username}"

    def __delete__(self, instance):
        storage = self.image.storage
        path = self.image.path
        super(Post, self).delete(instance)
        storage.delete(path)
