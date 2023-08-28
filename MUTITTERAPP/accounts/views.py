from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            pass
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"

    def form_invalid(self, form):
        messages.error(self.request, "Registration Failed")
        return super().form_invalid(form)
    