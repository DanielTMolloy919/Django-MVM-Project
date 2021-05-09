- [Django Tutorial](https://youtu.be/FN3EfKC2i6M)
- Remember to open the project as a workspace
- testing out the website - `python Ceberus/manage.py runserver`
- updating Django
  - `python manage.py makemigrations`
- format help

# Processes

## Adding A Page
1. Reference the page html file in the app's views.py
2. Link the view to a website url in the app's urls.py
3. Create the html file in the templates folder
4. Link the page in base.html or similar so it can be accessed by the user

## New App

1. Create new folder in apps

2. run `python manage.py <app_name> <app_location>` 

   e.g. `python manage.py startapp product apps/product`

3. add to settings.py INSTALLED_APPS as  `'apps.<app_name>.apps.<App_Name>Config'` 

   e.g. `'apps.product.apps.ProductConfig'` 

4. in apps.py change the AppConfig variable name to `'apps.<app_name>'`

   e.g. from`name = 'product'` to `name = 'apps.product'`

### Migrate New Models

1. run `python manage.py makemigrations`
2.  run `python manage.py migrate`



