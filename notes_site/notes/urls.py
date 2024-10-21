from django.urls import path
from . import views

urlpatterns=[
    path('notes/',views.NotesListView.as_view(), name="noteslist"),
    path('notes/<int:pk>/',views.NotesDetailView.as_view(),name="notesdetail"),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name="notesupdate"),
    path('notes/<int:pk>/delete',views.NotesDeleteView.as_view(),name="notesdelete"),
    path('notes/new',views.NotesCreateView.as_view(),name="notesnew"),
]