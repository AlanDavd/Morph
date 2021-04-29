"""User test related to model."""

# Pytest
import pytest

# Models
from morph.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_short_name(user: User):
    assert user.get_short_name() == user.username
