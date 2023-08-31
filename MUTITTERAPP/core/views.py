from django.shortcuts import render
from django.http import HttpResponse
from .models import Kling
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .forms import KlingForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import KlingFilter
from django.core.paginator import Paginator
from django.db.models.functions import Length

class Base(LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(Base, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class CreateKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("home")
    template_name = "create_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,"Klinged succesfully!")
        return super().form_valid(form)

class MyKling(ListView):
    model = Kling
    context_object_name = "klings"
    form_class = KlingForm
    success_url = reverse_lazy("my_klings")
    paginate_by = 4

    def get_queryset(self):
        queryset = super(MyKling, self).get_queryset().order_by('-created_on')
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        klings = context['klings']
        for kling in klings:
            kling.text = ' '.join(kling.text.split()[:50])
        return context

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

class MyKlingDelete(LoginRequiredMixin, DeleteView):
    model = Kling
    context_object_name = "kling"
    success_url = reverse_lazy("my_klings")

    def get_queryset(self):
        queryset = super(MyKlingDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class Home(FilterView):
    context_object_name = "klings"
    filterset_class = KlingFilter
    template_name = "homepage.html"
    paginate_by = 6
    
    def get_queryset(self):
        queryset = Kling.objects.order_by('-created_on')
        return queryset.annotate(text_length=Length('text'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        klings = context['klings']
        for kling in klings:
            kling.text = ' '.join(kling.text.split()[:50])
        return context

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request, pk):
    try:
        kling = Kling.objects.get(pk=pk)
    except Kling.DoesNotExist:
        return HttpResponse("Post not found.", status=404)
    context = {
        'kling': kling,
    }

    return render(request, 'post.html', context)

def kling_list(request):
    klings = Kling.objects.all() 
    paginator = Paginator(klings, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  }

    return render(request, 'kling_list.html', context)