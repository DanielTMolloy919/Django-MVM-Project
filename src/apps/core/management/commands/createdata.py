from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.repair.models import Category, RepairType
from apps.repair.views import Repair, repair 
import random, datetime
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.vendor.models import Vendor

categories = [
    'iPhone 8',
    'iPhone X',
    'Pixel 6',
    'Galaxy S21',
    'K51S',
    'Find X2 Neo',  
]

types = [
    'Screen Replacement',
    'Battery Replacement',
    'Headphone Jack Repair',
    'Power Button Repair',
    'Charging Port Repair'
]

vendors = [
    'Superior Phone Fix Service',
    'Mayfield Cell Phone Repairs',
    'iGenius Mobilefix',
    'Lambton Phones and Repairs',
    'Newcastle Mobile Phone Repairs',
    'Mobile Repair Central',
    'Mobile Experts Charlestown Shop',
]


def generate_price():
    return random.randint(0,300)

def generate_date_added():
    year = random.randint(2010,2020)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime.date(year,month,day)

def generate_rating():
    return random.uniform(0, 5)

def generate_review_count():
    return random.randint(0,10000)

def load_image():
    index = random.randint(0,4)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for x in range(6): #generate all dummy vendors
            vendor_name = vendors[x]
            
            
            file_name = str(x) + '.jpg'
            image_path = 'static/sample_data/' + file_name
            image =  SimpleUploadedFile(name=file_name, content=open(image_path, 'rb').read(), content_type='image/jpg')

            g_rating = generate_rating()
            g_review_count = generate_review_count()
            
            vendor = Vendor.objects.get_or_create(
                display_name = vendor_name,
                # created_at = generate_date_added,
                image = image,
                g_rating = g_rating,
                g_review_count = g_review_count
            )

            for y in range(5): # for each vendor, generate all the device categories
                category_name = categories[y]

                category = Category.objects.get_or_create(
                    name = category_name,
                    slug = slugify(category_name)
                )

                for z in range(4): # for each category, generate the possible repair types
                    type_name = types[z]

                    repair_type = RepairType.objects.get_or_create(
                        name = type_name,
                        slug = slugify(type_name)
                    )

                    price = generate_price()
                    date_added = generate_date_added()

                    repair = Repair(
                        category = Category.objects.get(name = category_name),
                        vendor = Vendor.objects.get(display_name = vendor_name),
                        repair_type = RepairType.objects.get(name = type_name),
                        price = price,

                        # date_added = date_added
                    )

                    repair.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
