from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, Textarea, EmailInput, PasswordInput

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            # 'first_name': TextInput(attrs={'class': 'form-control'}),
            # 'last_name': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),

        }


class ProfileForm(forms.ModelForm):
    """Creating Profile Form"""
    class Meta:
        """Customize Profile Form"""
        model = Profile

        fields = ['profile_name', 'address', 'image']

        exclude = ['user']

        widgets = {
            'profile_name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
        }





