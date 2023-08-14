from django.shortcuts import render
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
