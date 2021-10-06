import django_filters # Add filter addon

from .models import * # Importing all our models

class ProductFilter(django_filters.FilterSet):   # FilterSet enables the automatic generation of filters from a model
    class Meta:
        model = Product # defines which model to use
        fields = ['category','price'] # defines which model fields to use