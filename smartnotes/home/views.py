
from django.shortcuts import render
from django.http import HttpResponse
from datetime import time, datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html', {'now' : datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'authorized.html', {'now' : datetime.today()})
