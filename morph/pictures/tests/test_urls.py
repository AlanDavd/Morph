"""User URLs related tests."""

# Django
from django.urls import resolve, reverse

# Models
from morph.pictures.models import Post

# Pytest
import pytest

pytestmark = pytest.mark.django_db


def test_feed():
    assert reverse("pictures:feed") == "/"
    assert resolve("/").view_name == "pictures:feed"


def test_create():
    assert reverse("pictures:create") == "/pictures/new/"
    assert resolve("/pictures/new/").view_name == "pictures:create"
