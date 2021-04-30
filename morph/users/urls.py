"""User URLs."""

# Django
from django.urls import path

# Views
from morph.users.views import (
    UserDetailView,
    LoginView,
    LogoutView,
    SignUpView,
)

app_name = "users"
urlpatterns = [
    path(route="login/", view=LoginView.as_view(), name="login"),
    path(route="logout/", view=LogoutView.as_view(), name="logout"),
    path(route="signup/", view=SignUpView.as_view(), name="signup"),
    path(route="<str:username>/", view=UserDetailView.as_view(), name="detail"),
]
