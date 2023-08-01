from django.shortcuts import render

def signup_login(request):
    return render(request, "signup_login.html")


# Create your views here.
def home(request):
    return render(request, "home.html")