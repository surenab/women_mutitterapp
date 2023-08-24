from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
import re


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Given '{username}' username is already in use.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not re.search(r'[a-z]', password1) or not re.search(r'[A-Z]', password1) or \
            not re.search(r'[0-9]', password1) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise forms.ValidationError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data
