from typing import Any
from django import forms
from .models import Kling
from django.utils import timezone


class KlingForm(forms.ModelForm):
    """Class representing a Kling"""
    KLING_TYPES = (("1", "Hot"), ("2", "Standard"), ("3", "Relaxing"))
    KLING_CATEGORY = (
        ("Life and Love", "Life and Love"),
        ("Travel and Adventure", "Travel and Adventure"),
        ("Art and Music", "Art and Music"),
        ("Nature", "Nature"),
        ("Food and Wellness", "Food and Wellness"),
        ("Careers", "Careers"),
        ("Science and Technology", "Science and Technology"),
        ("Other", "Other"),
    )
   
    created_on = forms.DateTimeField(widget=forms.SelectDateWidget())
    title = forms.CharField(
         widget=forms.TextInput()
    )
    text = forms.CharField(
        widget=forms.Textarea()
    )
    kling_category = forms.ChoiceField(
        choices=KLING_CATEGORY, widget=forms.Select()
    )
    image = forms.ImageField()
    kling_types = forms.ChoiceField(choices=KLING_TYPES)
    
    """Docstring fot Meta."""

    class Meta:
        model = Kling
        fields = ("kling_category", "title", "text", "image")




