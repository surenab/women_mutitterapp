from django.shortcuts import render

# Create your views here.

def signup_login(request):
    return render(request, "signup_login.html")
