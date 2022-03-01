# Django-MVM-Project

This is a personal Django web project that is still being developed. The aim is to develop a fully functional multi-vendor ecommerce marketplace platform. The purpose of this project is to rapidly skill myself up with an ambitious project, in order to get practical and demonstratable skills. Foundational as well as more advanced skills this project will comprise include

https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8

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
- m1 issues https://github.com/psycopg/psycopg2/issues/1216#issuecomment-1044209371

### Setup Docker

- Run `docker-compose build` then `docker-compose up`
- Open Docker dashboard, find the db container and open the CLI
- run `psql -U postgres`
- Create psql user `CREATE USER admin WITH ENCRYPTED PASSWORD 'admin';`
- Create psql database `CREATE DATABASE "ceberus-db" WITH OWNER admin;`

https://forum.chirpstack.io/t/chirpstack-docker-image-cant-connect-to-postgres/10183/5

### Run

- `python3 manage.py run`

### Run Docker

- `docker-compose up`

## Other Functions

### Postgres Shell

`psql -U postgres`

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

https://github.com/sameersbn/docker-postgresql/issues/112

https://forum.chirpstack.io/t/chirpstack-docker-image-cant-connect-to-postgres/10183/3

### Terminal Access to Docker Container

- run `docker ps` and get the desired container's id
- `docker exec -t -i <CONTAINER_ID> bash`

https://stackoverflow.com/questions/62807717/how-can-i-solve-postgresql-scram-authentifcation-problem

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
