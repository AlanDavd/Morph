"""Picture related forms."""

# Django
from django import forms

# Models
from morph.pictures.models import Post


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""
        model = Post
        fields = ('owner', 'title', 'image')
