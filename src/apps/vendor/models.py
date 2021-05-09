from django.contrib.auth.models import User
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE) # linking venders to users, and making sure they get deleted when the users do

    class Meta: # this allows us to order by name
        ordering = ['name']
    
    def __str__(self): # this is a string representation - we see the vendor name instead of the object ID
        return self.name

class Test(models.Model):
    test_data = models.CharField(max_length=255)