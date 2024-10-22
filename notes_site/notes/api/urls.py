from django.urls import path
from . import views



urlpatterns=[
    path('',views.getRoutes),
    path('notes/',views.getNames),
    path('notes/create/', views.createNote), 
    path('note/<str:id>/', views.detailData),
    
    
    
]