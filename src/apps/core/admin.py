from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User

# @admin.register(CustomUser)
# class MyUserAdmin(UserAdmin):
#     add_fieldsets = (
#             (None, {
#                 'classes': ('wide',),
#                 'fields': ('email', 'password1', 'password2'),
#             }),
    # )