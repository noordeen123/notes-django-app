from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import notes
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm


class DeleteNotesView(DeleteView):
   template_name = 'delete.html'
   model = notes
   success_url = '/smart/notes/'
   

class UpdateNotesView(UpdateView):
   template_name = 'form.html'
   model = notes
   success_url = '/smart/notes/'
   form_class = NotesForm

class CreateNotesView(LoginRequiredMixin, CreateView):
   template_name = 'form.html'
   model = notes
   login_url = '/admin/'
   success_url = '/smart/notes/'
   form_class = NotesForm

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())

class ListNotesView(LoginRequiredMixin ,ListView):
   template_name = 'list.html'
   model = notes
   context_object_name = 'notes'
   login_url = '/admin/'

   def get_queryset(self):
      return self.request.user.notes_set.all()
 

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
