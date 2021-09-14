from django.shortcuts import render, get_list_or_404
from .models import Post
from django.views.generic import DetailView

def blog(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request, 'blog/blog.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'