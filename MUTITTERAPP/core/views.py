from django.shortcuts import render,redirect
from .models import Kling
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
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

    def get_queryset(self):
        queryset = super(MyKling, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


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

class MyKlingDetail( DetailView):
    model = Kling
    context_object_name = "kling"

    def get_queryset(self):
        queryset = super(MyKlingDetail, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

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
