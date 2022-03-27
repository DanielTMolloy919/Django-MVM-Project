from django import forms
from django.forms import ModelForm

from apps.repair.models import Repair
from apps.vendor.models import Vendor

class RepairForm(ModelForm): # display a form where the vendor can enter in the details of a repair for sale
    class Meta:
        model = Repair
        fields = ['category', 'repair_type', 'description', 'price']

class VendorCompletionForm(forms.Form):
    display_name = forms.CharField(label="Display Name", max_length=100)
    logo = forms.ImageField()
    website = forms.URLField(label="Website", max_length=200)


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["display_name"].widget.attrs.update({
            'id':'display_name',
            'class':'input'
        })
        self.fields["logo"].widget.attrs.update({
            'id':'logo',
            'class':'file-input',
            'onchange':'readURL(this);',
            'name': 'images'
        })
        self.fields["website"].widget.attrs.update({
            'id':'website',
            'class':'input'
        })
        
    class Meta:
        model=Vendor
        fields=['display_name','logo','website']