from django import forms
from .models import Kling,KlingComment, CommentReply, UserProfile
from .models import Message, SubscribedUsers


class KlingForm(forms.ModelForm):
    """Class representing a Kling"""
    
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

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'required': 'required'})
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = SubscribedUsers
        fields = ['email']