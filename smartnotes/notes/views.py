from django.shortcuts import render
from .models import notes

def list(request):
   all_notes = notes.objects.all()
   return render(request, 'list.html',{'notes':all_notes})

