from django.urls import path
from . import views

urlpatterns=[
    path('notes/',views.NotesListView.as_view(), name='noteslist'),
    path('notes/<int:pk>/',views.NotesDetailView.as_view(), name='notesdetail'),
]