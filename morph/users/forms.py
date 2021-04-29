"""User forms."""

# Django
from django import forms
from django.contrib.auth import get_user_model

# Auth set up
User = get_user_model()


class UserCreationForm(forms.Form):
    """User creation form.
    Basic user model creation.
    """
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """username must be unique."""
        username = self.cleaned_data['username']
        taken_username = User.objects.filter(username=username).exists()
        if taken_username:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean_email(self):
        """username must be unique."""
        email = self.cleaned_data['email']
        taken_email = User.objects.filter(email=email).exists()
        if taken_email:
            raise forms.ValidationError('Username is already in use.')
        return email

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        user.save()
