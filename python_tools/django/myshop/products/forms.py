# forms.py

from django import forms
from .models import Product, VariantType, Variant

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'stock', 'description', 'details']

class VariantTypeForm(forms.ModelForm):
    class Meta:
        model = VariantType
        fields = ['name']

class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ['type', 'name', 'price', 'stock']
