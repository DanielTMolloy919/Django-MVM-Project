from django.db import models
from django.db.models.fields import related
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify

from apps.vendor.models import Vendor

# class Category(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255) # effectively a url
#     ordering = models.IntegerField(default=0) # this changes the ordering of the categories on the home page header

#     class Meta:
#         ordering = ['ordering'] # this orders the categories based on the ordering value
    
#     def __str__(self):
#         return self.title

class Category(MPTTModel): # this is the device that is being repaired e.g. Galaxy S8
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255) # effectively a url
    ordering = models.IntegerField(default=0) # this changes the ordering of the categories on the home page header
    
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children') # stuff todo with making the categories hierarchical

    class MPTTMeta: # adjusts how the categories should be ordered
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): # overriding the save function to auto-add a category slug
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

# class Repair(models.Model):
#     category = models.ForeignKey(Category, related_name='repairs', on_delete=models.CASCADE) # this is sort of like a one to one field, except that repairs can have more than one category. As such, this allows us to get all the repairs in a category
#     vendor = models.ForeignKey(Vendor, related_name='repairs', on_delete=models.CASCADE) # This will allow us to get all the repairs of a vendor   

class RepairType(models.Model): # This is the type of repair being done, e.g. screen repair
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255) # effectively a url

    def __str__(self):
        return self.name
    
class Repair(models.Model): # This is the individual, purchasable repair
    category = models.ForeignKey(Category, related_name='repairs', on_delete=models.CASCADE) # inherit a single category
    vendor = models.ForeignKey(Vendor, related_name='repairs', on_delete=models.CASCADE) # inherit a single vendor
    repair_type = models.ForeignKey(RepairType, related_name='repairs', on_delete=models.CASCADE) # inherit a single repair type
    slug = models.SlugField(max_length=255) # effectively a url
    description = models.TextField(blank=True, null=True) # a repair description, which can be left blank
    price = models.DecimalField(max_digits=6, decimal_places=2) # the best way to store currency values
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def get_rating(self):
        return round(self.vendor.g_rating,1)

    def get_star_rating(self):
        rounded_rating = round(self.vendor.g_rating * 2) / 2
        return "star_" + str(rounded_rating)

    def get_review_count(self):
        return self.vendor.g_review_count
    
    def __str__(self):
        return self.vendor.name + " " + self.category.name + " " + self.repair_type.name


