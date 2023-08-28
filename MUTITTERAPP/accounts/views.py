from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages

class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"

    def form_invalid(self, form):
        messages.error(self.request, "Registration Failed")
        return super().form_invalid(form)
    