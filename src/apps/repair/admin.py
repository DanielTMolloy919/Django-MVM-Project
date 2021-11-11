from django.contrib import admin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Repair, RepairType

# admin.site.register(Category)
admin.site.register(Repair)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(RepairType)