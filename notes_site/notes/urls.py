from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_note, name='add_note'),
    path('view/', views.view_notes, name='view_notes'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
