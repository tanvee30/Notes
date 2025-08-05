# home/views.py
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required




def register_view(request):
    return render(request, 'home/register.html')

def home_view(request):
    return render(request, 'home/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # you can change this to 'login' if needed
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'home/login.html'

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')