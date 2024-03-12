from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm
# Create your views here.

class SignupView(CreateView):
  model = User
  form_class = SignupForm
  template_name ='signup.html'
  success_url = reverse_lazy('index')

def logout_view(request):
  logout(request)
  return redirect('index')
