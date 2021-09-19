from django.urls import path
from . import views
from.views import PostDetailView, PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-details'),
]