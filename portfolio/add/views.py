from django.shortcuts import render
from .models import Portfolio, Project

# Create your views here.

def portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, "add/portfolio.html", {"portfolio": portfolio})

def projects(request):
    projects = Project.objects.all()   
    return render(request, "add/projects.html", {"projects": projects})