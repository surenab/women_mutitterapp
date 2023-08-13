from django.shortcuts import render
from .models import Kling
from django.views.generic import CreateView
from .forms import KlingForm
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    klings = Kling.objects.all()
    return render(request=request, template_name="homepage.html", context={"klings": klings})


class CreateKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("post")
    template_name = "create_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Your Kling is Successfully Created!")
        messages.error(self.request, "Klinging failed")
        return super().form_valid(form)
