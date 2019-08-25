# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.forms import TextInput, Select, Textarea, EmailInput, PasswordInput
#
#
# class SignUpForm(UserCreationForm):
#     address = forms.CharField(max_length=150)
#
#     class Meta:
#         model = User
#
#         fields = ['first_name', 'last_name', 'username', 'address', 'email', 'password1', 'password2']
#
#         widgets = {
#             'first_name': TextInput(attrs={'class': 'form-control'}),
#             'last_name': TextInput(attrs={'class': 'form-control'}),
#             'username': TextInput(attrs={'class': 'form-control'}),
#             'address': TextInput(attrs={'class': 'form-control'}),
#             'email': EmailInput(attrs={'class': 'form-control'}),
#             'password1': PasswordInput(attrs={'class': 'form-control'}),
#             'password2': PasswordInput(attrs={'class': 'form-control'}),
#
#         }
#
#
#
#
#
#
#
#
#
