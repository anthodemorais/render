from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView

from .models import Project

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'render_app/signup.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        projects_count = Project.objects.filter(user_ids=request.user.id).count()
        if projects_count == 0:
            return render(request, 'render_app/home.html', {"projects": None, 'authenticated':True})
        else:
            projects = Project.objects.filter(user_ids=request.user.id)
            return render(request, 'render_app/home.html', {"projects": projects, 'authenticated':True})            
    else:
        return render(request, 'render_app/home.html', {"projects": None, 'authenticated':False})

class ProjectsListView(ListView):
    model = Project
    context_object_name = "projects"

class ProjectsDetailView(DetailView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = "project"