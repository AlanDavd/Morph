"""Factory tests."""

# Factory
from factory import Faker
from factory.django import DjangoModelFactory

# Model
from morph.pictures.models import Post


class PostFactory(DjangoModelFactory):

    title = Faker("title")
    image = Faker("image")
    owner = Faker("owner")

    class Meta:
        model = Post
