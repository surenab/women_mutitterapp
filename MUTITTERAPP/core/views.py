from django.shortcuts import render
from .models import Kling
from django.views.generic import CreateView, DeleteView
from .forms import KlingForm
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    klings = Kling.objects.all()
    return render(request=request, template_name="homepage.html", context={"klings": klings}
    )


class CreateKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("post")
    template_name = "create_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Your Kling is Successfully Created!")
        messages.error(self.request, "Klinging failed")
        return super().form_valid(form)
    
class MyKlingDelete(LoginRequiredMixin, DeleteView):
    model = Kling
    context_object_name = "kling"
    success_url = reverse_lazy("my_klings")

    def get_queryset(self):
        queryset = super(MyKlingDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.info(self.request, "Kling deleted!")
        return super().form_valid(form)
