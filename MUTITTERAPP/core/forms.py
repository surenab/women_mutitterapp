from typing import Any
from django import forms
from .models import Kling,KlingComment, KlingReply 
from django.utils import timezone
from .models import Message


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
    
    class Meta:
        model = Kling
        fields = ("kling_category", "title", "text", "image")


class MessageForm(forms.ModelForm):
    full_name = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=150, required=True)
    message = forms.CharField(max_length=700, required=True)

    class Meta:
        model = Message
        exclude = ()

class KlingCommentForm(forms.ModelForm):
    widgets = {'text': forms.Textarea(attrs={'rows': 6}),}
    class Meta:
        model = KlingComment
        fields = ["text"]

class KlingReplyForm(forms.ModelForm):
    comment_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = KlingReply
        fields = ['text']