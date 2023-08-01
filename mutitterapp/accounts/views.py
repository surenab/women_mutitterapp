from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm


def signup_login(request):
    return render(request, "register.html")

def home(request):
    return render(request, "home.html")

class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "register.html" 

