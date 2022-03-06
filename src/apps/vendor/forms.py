from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from apps.repair.models import Repair


class RepairForm(ModelForm): # display a form where the vendor can enter in the details of a repair for sale
    class Meta:
        model = Repair
        fields = ['category', 'repair_type', 'description', 'price']

class BecomeVendorForm(UserCreationForm):

    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
