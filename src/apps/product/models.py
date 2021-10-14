from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.vendor.models import Vendor

# class Category(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255) # effectively a url
#     ordering = models.IntegerField(default=0) # this changes the ordering of the categories on the home page header

#     class Meta:
#         ordering = ['ordering'] # this orders the categories based on the ordering value
    
#     def __str__(self):
#         return self.title

class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255) # effectively a url
    ordering = models.IntegerField(default=0) # this changes the ordering of the categories on the home page header
    

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children') # stuff todo with making the categories heirarchical

    class MPTTMeta: # adjusts how the categories should be ordered
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name

# class Repair(models.Model):
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # this is sort of like a one to one field, except that products can have more than one category. As such, this allows us to get all the products in a category
#     vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE) # This will allow us to get all the products of a vendor   

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # this is sort of like a one to one field, except that products can have more than one category. As such, this allows us to get all the products in a category
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE) # This will allow us to get all the products of a vendor
    title = models.CharField(max_length=255) # title of the product
    slug = models.SlugField(max_length=255) # effectively a url
    description = models.TextField(blank=True, null=True) # a product description, which can be left blank
    price = models.DecimalField(max_digits=6, decimal_places=2) # the best way to store currency values
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title