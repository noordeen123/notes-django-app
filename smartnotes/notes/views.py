from django.shortcuts import render
from django.http import Http404
from .models import notes
from django.views.generic import ListView, DetailView, TemplateView

class ListNotesView(ListView):
   template_name = 'list.html'
   model = notes
   context_object_name = 'notes'
 

# def list(request):
#    all_notes = notes.objects.all()
#    return render(request, 'list.html',{'notes':all_notes})

class DetailsNotesView(DetailView):
   template_name = 'details.html'
   model = notes
   context_object_name = 'note'
   
   



# def details(request, id):
#    try:
#       note = notes.objects.get(pk=id)
#    except notes.DoesNotExist:
#       raise Http404('Note not found')
#    return render(request, 'details.html', {'note':note})
