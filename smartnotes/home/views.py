
from django.shortcuts import render
from django.http import HttpResponse
from datetime import time, datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'now' : datetime.today()}


# class AuthorizedView(TemplateView, LoginRequiredMixin):
#     login_url = '/login/'
#     template_name = 'authorized.html'

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'
    login_url = '/admin/'

# @login_required(login_url='/admin/')
# def AuthorizedView(request):
#     return render(request, 'authorized.html')
    

