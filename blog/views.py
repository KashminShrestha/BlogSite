# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from blog.models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = "__all__"


class BlogUpdateView(UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "post_edit.html"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
