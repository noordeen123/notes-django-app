from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list, name='list'),
    # path('notes/<int:id>', views.details, name='details')
    path('notes', views.ListNotesView.as_view(), name='list'),
    path('notes/<int:pk>', views.DetailsNotesView.as_view(), name='details')
]