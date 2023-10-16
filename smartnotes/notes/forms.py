from django import forms
from django.core.exceptions import ValidationError
from .models import notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb5'}),
        }
        labels = {
            'title': 'Your Note Title',
            'text': 'Your Note',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError('Title must be at least 3 characters long')
        return title
            