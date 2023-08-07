# Create your views here.
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cackling
from django.views.generic import CreateView
from .forms import CacklingForm
from django.urls import reverse_lazy


def home(request):
    cacklings = Cackling.objects.all()

    return render(
        request=request, template_name="home.html", context={"cacklings": cacklings}
    )


class CreateCackling(CreateView):
    form_class = CacklingForm
    success_url = reverse_lazy("home")
    template_name = "create_cackling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
