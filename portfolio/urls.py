from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='port-home'),
    path('about', views.about, name='port-about'),
    path('resume', views.resume, name='port-resume')

]