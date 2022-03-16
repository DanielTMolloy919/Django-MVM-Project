from turtle import Vec2D
from apps.vendor.models import Vendor 
from apps.repair.models import Category, RepairType, Repair
from apps.core.models import User

def clear_database():
    Vendor.objects.all().delete()
    Category.objects.all().delete()
    RepairType.objects.all().delete()
    Repair.objects.all().delete()
    User.objects.all().delete()