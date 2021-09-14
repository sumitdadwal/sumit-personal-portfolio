from django.urls import path
from . import views
from.views import PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-details'),
]