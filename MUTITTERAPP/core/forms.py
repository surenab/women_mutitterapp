from typing import Any
from django import forms
from .models import Cackling


class CacklingForm(forms.ModelForm):
    CACKLING_TYPES = (("1", "Hot"), ("2", "Standard"), ("3", "Relaxing"))
    cackling_type = forms.ChoiceField(choices=CACKLING_TYPES)
    submit_date = forms.DateTimeField(widget=forms.SelectDateWidget())

    class Meta:
        model = Cackling
        fields = (
            "submit_date",
            "category",
            "title",
            "text",
            "cackling_type",
        )

    def save(self, commit: bool = ...) -> Any:
        obj = super(CacklingForm, self).save
        return super().save(commit)
