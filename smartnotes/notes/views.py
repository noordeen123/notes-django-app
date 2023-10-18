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

class CreateNotesView(CreateView):
   template_name = 'form.html'
   model = notes
   success_url = '/smart/notes/'
   form_class = NotesForm

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())

class ListNotesView(LoginRequiredMixin, ListView):
   login_url = '/login/'
   template_name = 'list.html'
   model = notes
   context_object_name = 'notes'
   

   def get_queryset(self):
      return self.request.user.notes_set.all()
 



class DetailsNotesView(DetailView):
   template_name = 'details.html'
   model = notes
   context_object_name = 'note'
   



