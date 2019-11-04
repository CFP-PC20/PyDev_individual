from django.shortcuts import render
from django.http import HttpResponse
from avisos.models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    
    return render(request, 'index.html', context)

def spain(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    
    return render(request, 'spain.jpg', context)