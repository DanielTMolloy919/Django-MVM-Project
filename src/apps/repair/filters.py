import django_filters # Add filter addon

from .models import Repair # Importing all our models

class RepairFilter(django_filters.FilterSet):   # FilterSet enables the automatic generation of filters from a model
    # thumbnail = ModelChoiceFilter(queryset=Author.objects.all())
    
    class Meta:
        model = Repair # defines which model to use
        fields = ['category','price'] # defines which model fields to use