from django.forms import ModelForm

from apps.product.models import Product

class ProductForm(ModelForm): # display a form where the vendor can enter in the details of a product for sale
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price']