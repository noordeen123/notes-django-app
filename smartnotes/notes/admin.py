from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title', 'text')
    list_filter = ('created', 'id', 'title')

  
                
admin.site.register(models.notes, NotesAdmin)