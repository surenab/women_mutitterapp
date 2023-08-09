from typing import Any
from django import forms
from .models import Kling
from django.utils import timezone


class KlingForm(forms.ModelForm):
    KLING_TYPES = (("1", "Hot"), ("2", "Standard"), ("3", "Relaxing"))
    cackling_type = forms.ChoiceField(choices=KLING_TYPES)

    class Meta:
        model = Kling
        fields = (
            "category",
            "title",
            "text",
            "cackling_type",
        )
