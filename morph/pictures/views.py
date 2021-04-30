"""Pictures views."""

# Django
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, View

# Forms
from morph.pictures.forms import PostForm

# Models
from morph.pictures.models import Post
User = get_user_model()


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""
    template_name = 'pictures/new.html'
    form_class = PostForm
    success_url = reverse_lazy('pictures:feed')

    def get_context_data(self, **kwargs):
        """Add user to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        """Handle bulk image uploading."""
        user = request.POST.get('owner', '')
        title = request.POST.get('title', '')
        images = request.FILES.getlist("image")
        for file in images:
            instance = Post(
                owner=User.objects.get(pk=user),
                title=title,
                image=file,
            )
            instance.save()
        return HttpResponseRedirect(self.success_url)


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts and a way to bulk delete them."""
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'
    template_name = 'pictures/feed.html'

    def get(self, request, *args, **kwargs):
        """Return all posts."""
        return super(PostsFeedView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Perform bulk delete of selected entries."""
        if request.method == "POST":
            post_ids = request.POST.getlist("id[]")
            filtered = filter(lambda id: id != 'on', post_ids)
            for id in filtered:
                post = Post.objects.get(pk=id)
                post.delete()
            return render(request, "pictures/feed.html", {})


class DeletePost(LoginRequiredMixin, DeleteView):
    """Delete only one picture post view."""
    model = Post
    success_url = reverse_lazy('pictures:feed')
    success_message = 'Deleted Successfully'
    template_name = 'pictures/confirm_delete.html'
    context_object_name = 'post'
