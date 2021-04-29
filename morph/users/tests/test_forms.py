"""Module for all Form Tests."""

# Forms
from morph.users.forms import UserCreationForm

# Models
from morph.users.models import User

# Pytest
import pytest

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    """Test class for all tests related to the UserCreationForm."""

    def test_username_validation_error_msg(self, user: User):
        """
        Tests UserCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing username cannot be added.
            2) A new user with an existing email cannot be added.
            3) 1 or more errors are raised by the UserCreation Form
            4) The desired error message is raised
        """

        # The user already exists, hence cannot be created.
        form = UserCreationForm({
            "username": user.username,
            "password": user.password,
            "password_confirmation": user.password,
        })

        assert not form.is_valid()
        assert len(form.errors) == 4
        assert "username" in form.errors
        assert form.errors["username"][0] == "Username is already in use."
