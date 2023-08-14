# Create your views here.
from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import Kling
from django.views.generic import CreateView
from .forms import KlingForm
from django.urls import reverse_lazy


def home(request):
    klings = Kling.objects.all()
    return render(request=request, template_name="homepage.html", context={"klings": klings}
    )


class CreateKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("home")
    template_name = "create_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MyKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("home")
    template_name = "my_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
