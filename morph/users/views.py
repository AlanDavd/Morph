"""User views."""

# Django
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, FormView

# Forms
from morph.users.forms import UserCreationForm

# User set up
User = get_user_model()


class SignUpView(FormView):
    """Users sign up view creates a normal (non admin) user."""

    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Users sign up view."""

    template_name = "users/login.html"


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Log out view."""

    template_name = "pages/logged_out.html"


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    # model = User
    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        """Add extra info to context."""
        context = super().get_context_data(**kwargs)
        return context


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
