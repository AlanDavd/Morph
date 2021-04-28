"""User views."""

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

# User set up
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view allows logged in user to view the
    details of a model.
    """
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """User update view allows logged in user to update
    it's information.
    """
    model = User
    fields = ["username"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """Redirect view to detail view."""
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})
