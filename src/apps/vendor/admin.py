from django.contrib import admin

# Register your models here.
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')

admin.site.register(Vendor)