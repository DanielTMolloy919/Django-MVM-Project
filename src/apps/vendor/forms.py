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

    # used to edit the CSS/HTML of the form input fields
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'id':'username',
            'class':'input'
        })
        self.fields["email"].widget.attrs.update({
            'id':'email',
            'class':'input'
        })
        self.fields["password1"].widget.attrs.update({
            'id':'password1',
            'class':'input'
        })
        self.fields["password2"].widget.attrs.update({
            'id':'password2',
            'class':'input'
        })

    class Meta:
        model=User
        fields=['username','email','password1','password2']
