from django.forms import ModelForm
from main.models import Product
from django import forms   
from django.contrib.auth.models import User   # NEW!

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name","price","description"]
        user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)  # NEW 