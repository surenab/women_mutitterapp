from django.shortcuts import render,redirect
from .models import Kling
from django.views.generic import CreateView
from .forms import KlingForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import KlingFilter




class Base(LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(Base, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

def home(request):
    klings = Kling.objects.all()
    return render(request=request, template_name="homepage.html", context={"klings": klings})


class CreateKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("home")
    template_name = "create_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Your Kling is Successfully Created!")
        messages.error(self.request, "Klinging failed")
        return super().form_valid(form)


    def create_kling(request):
        if request.method == 'POST':
            form = KlingForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('home')
        else:
            form = KlingForm()
        
        return render(request, 'post.html', {'form': form})
    
    
    
    class Home(FilterView):
        context_object_name="klings"
        filterset_class=KlingFilter
        template_name="homepage.html"
       
    
    class MyKlings( FilterView):
        context_object_name="klings"
        filterset_class=KlingFilter
        template_name="core/kling_list.html"
