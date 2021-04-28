"""User URLs."""

# Django
from django.urls import path

# Views
from morph.users.views import (
    DetailView,
    RedirectView,
    UpdateView
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=RedirectView.as_view(), name="redirect"),
    path("~update/", view=UpdateView.as_view(), name="update"),
    path("<str:username>/", view=DetailView.as_view(), name="detail"),
]
