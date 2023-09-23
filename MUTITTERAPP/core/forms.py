from django import forms
from .models import Kling,KlingComment, CommentReply, UserProfile
from .models import Message, SubscribedUsers
from django.contrib.auth.forms import SetPasswordForm


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

class UserPasswordChangeForm(SetPasswordForm):
    """
    For changing password
    """
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.user
        if user.check_password(old_password):
            return old_password
        else:
            raise forms.ValidationError("The old password is incorrect.")

    def __init__(self, *args, **kwargs):
        """
        updating form
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })        