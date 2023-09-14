from django import forms
from .models import Kling,KlingComment, KlingReply, UserProfile
from .models import Message, SubscribedUsers


class KlingForm(forms.ModelForm):
    """Class representing a Kling"""
    
    KLING_CATEGORY = (
        ("1","Life and Love" ),
        ("2","Travel and Adventure" ),
        ("3","Art and Music" ),
        ("4","Nature" ),
        ("5","Food and Wellness" ),
        ("6", "Careers"),
        ("7","Science and Technology" ),
        ("8","Other" ),
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = SubscribedUsers
        fields = ['email']