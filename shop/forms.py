from django import forms
from .models import *
class ShopProfileForm(forms.ModelForm):
    class Meta:
        model=ShopProfile
        exclude=('user',)