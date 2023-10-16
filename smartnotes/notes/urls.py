from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list, name='list'),
    # path('notes/<int:id>', views.details, name='details')
    path('notes/', views.ListNotesView.as_view(), name='list'),
    path('notes/<int:pk>/', views.DetailsNotesView.as_view(), name='details'),
    path('notes/<int:pk>/update/', views.UpdateNotesView.as_view(), name='update'),
    path('create/', views.CreateNotesView.as_view(), name='create'),
    path('notes/<int:pk>/delete/', views.DeleteNotesView.as_view(), name='delete'),
]