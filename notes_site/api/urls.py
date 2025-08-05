# api/urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),
    path('login/', obtain_auth_token, name='api_token_auth'),  # POST with username & password to get token
]
