
from django.shortcuts import render
from django.http import HttpResponse
from datetime import time, datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


from django.shortcuts import render, redirect






class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/login/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/smart/notes/')
        return super().get(request, *args, **kwargs)

    
    

class Logout(LogoutView):
    template_name = 'logout.html'
    
class Login(LoginView):
    template_name = 'login.html'
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect('/smart/notes/')
        return response
    
class BaseView(TemplateView):
    template_name = 'base.html'
    

class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'time': datetime.now()}

    

