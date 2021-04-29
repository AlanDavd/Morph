"""User URLs related tests."""

# Django
from django.urls import resolve, reverse

# Models
from morph.users.models import User

# Pytest
import pytest

pytestmark = pytest.mark.django_db


def test_login():
    assert reverse("users:login") == "/users/login/"
    assert resolve("/users/login/").view_name == "users:login"


def test_signup():
    assert reverse("users:signup") == "/users/signup/"
    assert resolve("/users/signup/").view_name == "users:signup"


def test_logout():
    assert reverse("users:logout") == "/users/logout/"
    assert resolve("/users/logout/").view_name == "users:logout"
