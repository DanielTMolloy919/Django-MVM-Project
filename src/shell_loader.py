import os

from apps.vendor.models import Vendor 
from apps.repair.models import Category, RepairType, Repair
from apps.core.models import User

def clear_database(test_data):
    Vendor.objects.all().delete()
    Category.objects.all().delete()
    RepairType.objects.all().delete()
    Repair.objects.all().delete()
    User.objects.all().delete()

    os.system('rm -rf media/uploads/')

    if (test_data):
        os.system('python manage.py createdata')
