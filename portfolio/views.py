from django.shortcuts import render
from .models import TechStack, Project
def home(request):
    techstacks = TechStack.objects.all()
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'techstacks': techstacks, 'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html', {})

def resume(request):
    return render(request, 'portfolio/resume.html', {})
