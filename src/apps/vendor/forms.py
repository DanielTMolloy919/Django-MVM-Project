from django import forms
from django.forms import ModelForm

from apps.repair.models import Repair

class RepairForm(ModelForm): # display a form where the vendor can enter in the details of a repair for sale
    class Meta:
        model = Repair
        fields = ['category', 'repair_type', 'description', 'price']