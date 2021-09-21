from django.contrib import admin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product

# admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Category, MPTTModelAdmin)