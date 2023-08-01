from django.shortcuts import render
from django.http import HttpResponse

def signup_login(request):
    return render(request, "signup_login.html")

def home(request):
    return HttpResponse("home/")

# Create your views here.
