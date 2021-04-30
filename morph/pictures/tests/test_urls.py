"""User URLs related tests."""

# Pytest
import pytest

# Django
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_feed():
    assert reverse("pictures:feed") == "/"
    assert resolve("/").view_name == "pictures:feed"


def test_create():
    assert reverse("pictures:create") == "/pictures/new/"
    assert resolve("/pictures/new/").view_name == "pictures:create"
