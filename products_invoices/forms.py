from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import (

    Select,
    Textarea,
    DateInput,
    TextInput,
    EmailInput,
    NumberInput,
    PasswordInput,
    SelectDateWidget,

)

from .models import Customer, Product, Invoice


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = ['customer_name', 'address', 'email']
        # fields = '__all__'

        widgets = {
            'customer_name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),

        }


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ['product_name', 'category', 'description']

        widgets = {
            'product_name': TextInput(attrs={'class': 'form-control'}),
            'category': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),

        }


class CreateInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

        fields = ['customer', 'currency', 'date', 'item_code', 'item_description', 'quantity', 'unit_price',
                  'discount']

        widgets = {
            'customer': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'date': SelectDateWidget(attrs={'class': 'custom-select'}),
            'item_code': TextInput(attrs={'class': 'custom-select'}),
            'item_description': Select(attrs={'class': 'custom-select'}),
            'quantity': NumberInput(attrs={'class': 'custom-select'}),
            'unit_price': NumberInput(attrs={'class': 'custom-select'}),
            'discount': NumberInput(attrs={'class': 'custom-select'}),
            # 'total': NumberInput(attrs={'class': 'custom-select'}),

        }

