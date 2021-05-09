from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import VendorSerializer

from .models import Vendor # importing our vendors database 
from apps.product.models import Product 

from .forms import ProductForm

def become_vendor(request):
    if request.method == 'POST': # this checks whether the sign up form has been submitted 
        form = UserCreationForm(request.POST) # pushing all the data we just collected into an object called 'form'

        if form.is_valid(): # executes if the user entered their data correctly
            user = form.save() # saves collected data to a new user object

            login(request, user) # logs in the newly created user

            vendor = Vendor.objects.create(name=user.username, created_by=user) # copies over the collected data to create a vendor object

            return redirect('frontpage') # pushes the user back to the front page
    else:
        form = UserCreationForm() # creates an empty form

    return render(request, 'vendor/become_vendor.html', {'form': form}) # make the form accessible by the front end html

@login_required # this checks if the user has already logged in, if not the user will be redirected to the login page
def vendor_admin(request): # code for the vendor interface
    vendor = request.user.vendor # loads the vendor object through the user model
    products = vendor.products.all() # importing all the products associated with a vendor

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products})


@login_required
def add_product(request):
    if request.method == 'POST': # if the product entry form has already been submitted
        form = ProductForm(request.POST, request.FILES) # put all the data collected into the form object

        if form.is_valid(): # if the user entry is valid then create the product
            product = form.save(commit=False) # we havent specficied who the vendor is yet, so we need to set commit to False
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin') # return the uesr to the admin dashboard
    else: # if it hasn't been filled, create an empty form
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form}) # render the empty form for the user to fill in

class VendorView(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()