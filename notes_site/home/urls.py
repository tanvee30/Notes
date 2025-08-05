# home/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # NEW
    
]
