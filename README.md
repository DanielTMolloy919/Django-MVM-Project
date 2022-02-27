# Django-MVM-Project

This is a personal Django web project that is still being developed. The aim is to develop a fully functional multi-vendor ecommerce marketplace platform. The purpose of this project is to rapidly skill myself up with an ambitious project, in order to get practical and demonstratable skills. Foundational as well as more advanced skills this project will comprise include

- General Django proficiency
- Interaction with SQL database using Django forms
- Advanced site searching and filtering
- Admin account structures and management
- Hashing and other web security tools
- Search engine optimisation
- Web Sockets
- Geolocation
- Payment APIs

### Setup

- Setup python environment `python3 -m venv env`
- Run environment `source env/bin/activate`
- Install packages `pip3 install -r requirements.txt`

### Run

- `python3 manage.py run`

### Run Docker

- `docker-compose up`

## Other Functions

### Migrate New Models

1. run `python manage.py makemigrations`
2. run `python manage.py migrate`

### Django Admin

https://youtu.be/PD3YnPSHC-c

1. In the src folder run `python manage.py shell`
2. Import your desired model e.g. `from apps.vendor.models import Vendor` `from apps.product.models import Product`
3. Useful commands
   - Retrieve all objects `Product.objects.all()`
   - Delete one object `Product.objects.filter(title='test').delete()`
   - Print object attribute `Product.objects.filter(title='test').vendor`
