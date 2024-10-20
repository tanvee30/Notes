from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name='home/welcome.html'

class AuthorizedViews(LoginRequiredMixin,TemplateView):
    template_name='home/authorized.html'
    login_url='/admin'

