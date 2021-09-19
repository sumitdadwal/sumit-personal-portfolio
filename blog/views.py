from django.shortcuts import render, get_list_or_404
from .models import Post
from django.views.generic import DetailView, ListView

# def blog(request, *args, **kwargs):
#     posts = Post.objects.all()
#     return render(request, 'blog/blog.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'