"""Factory tests."""

# Model
from morph.pictures.models import Post

# Factory
from factory import Faker, post_generation
from factory.django import DjangoModelFactory


class PostFactory(DjangoModelFactory):

    title = Faker("title")
    image = Faker("image")
    owner = Faker("owner")

    class Meta:
        model = Post
