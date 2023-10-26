from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User_human
from .forms import User_human_Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class UserListView(ListView):
    model = User_human
    template_name = 'user_list.html'
    context_object_name = 'users'
    # 

class UserCreateView(CreateView):
    model = User_human
    form_class = User_human_Form
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')
    # 

class UserDetailView(DetailView):
    model = User_human
    template_name = 'user_detail.html'
    context_object_name = 'user'
    # 

class Sign_Up(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')
    # 

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'user_list'
    # 

class Log_out(LogoutView):
    next_page = '/'