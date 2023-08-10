# Create your views here.
from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import Kling
from django.views.generic import CreateView,UpdateView
from .forms import KlingForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



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
    
    
class MyKlingUpdate(LoginRequiredMixin, UpdateView):
    model = Kling
    context_object_name = "kling"
    form_class = KlingForm
    success_url = reverse_lazy("my_klings")

    def get_queryset(self):
        queryset = super(MyKlingUpdate, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.success(self.request, "Kling instance is updated!")
        return super().form_valid(form)

    
