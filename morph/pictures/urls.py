"""Pictures URLs."""

# Views
from morph.pictures.views import PostsFeedView, CreatePostView, DeletePost

# Django
from django.urls import path

urlpatterns = [
    path(route="", view=PostsFeedView.as_view(), name="feed"),
    path(route="pictures/new/", view=CreatePostView.as_view(), name="create"),
    path(route=r"delete/<int:pk>/", view=DeletePost.as_view(), name="delete"),
]
