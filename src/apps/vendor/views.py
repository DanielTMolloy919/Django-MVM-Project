from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Vendor # importing our vendors database 
from apps.repair.models import Repair 

from .forms import RepairForm
from apps.core.forms import RegisterForm
from apps.vendor.forms import VendorCompletionForm

def become_vendor(request):
    if request.method == 'POST': # this checks whether the sign up form has been submitted 
        form = RegisterForm(request.POST) # pushing all the data we just collected into an object called 'form'

        if form.is_valid(): # executes if the user entered their data correctly
            user = form.save() # saves collected data to a new user object

            login(request, user) # logs in the newly created user

            vendor = Vendor.objects.create(email=user.email, display_name=user.name ,created_by=user) # copies over the collected data to create a vendor object

            request.session['vendor'] = vendor

            return finish_signup(request) # pushes the user back to the front page
            
    else:
        form = RegisterForm() # creates an empty form

    return render(request, 'vendor/become_vendor.html', {'form': form}) # make the form accessible by the front end html

@login_required
def finish_signup(request):
    vendor = request.session['vendor']

    if request.method == 'POST': # this checks whether the sign up form has been submitted 
        form = VendorCompletionForm(request.POST, request.FILES) # pushing all the data we just collected into an object called 'form'

        if form.is_valid(): # executes if the user entered their data correctly

            # vendor = Vendor.objects.filter(email='test@test.com')[0]

            vendor.display_name = form['display_name'].value()
            vendor.image = form['logo'].value()
            vendor.link = form['website'].value()

            vendor.save()

            return redirect('vendor_admin')# pushes the user back to the front page
            
    else:
        form = VendorCompletionForm() # creates an empty form

    return render(request, 'vendor/signup.html', {'vendor': vendor})



@login_required # this checks if the user has already logged in, if not the user will be redirected to the login page
def vendor_admin(request): # code for the vendor interface
    vendor = request.user.vendor # loads the vendor object through the user model
    repairs = vendor.repairs.all() # importing all the repairs associated with a vendor

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'repairs': repairs})

@login_required
def edit_profile(request): # This allows a vendor to edit their profile objects, e.g. icon, thumbnail etc.

    # if request.method == 'POST': # if the repair entry form has already been submitted
    #     form = UserChangeForm(request.POST, request.FILES) # put all the data collected into the form object

    #     if form.is_valid(): # if the user entry is valid then create the repair
    #         profile = form.save
    #         repair.vendor = request.user.vendor
    #         repair.slug = slugify(repair.title)
    #         repair.save()

    #         return redirect('vendor_admin') # return the uesr to the admin dashboard
    # else: # if it hasn't been filled, create an empty form
    #     form = UserChangeForm()
    
    return render(request, 'vendor/edit_profile.html',) # {'form': form}

@login_required
def add_repair(request):
    success = False
    if request.method == 'POST': # if the repair entry form has already been submitted
        form = RepairForm(request.POST, request.FILES) # put all the data collected into the form object

        if form.is_valid(): # if the user entry is valid then create the repair
            repair = form.save(commit=False) # we haven't specified who the vendor is yet, so we need to set commit to False
            repair.vendor = request.user.vendor
            repair.slug = slugify(repair.title)
            repair.save()

            # redirectUrl = reverse('add_repair') + "?success=True"

            return HttpResponseRedirect('/vendor/add-repair?success=True') # return the user to the admin dashboard
    else: # if it hasn't been filled, create an empty form
        form = RepairForm()
        if 'success' in request.GET: # if the repair just got added, show a success page, toggled on by the 'success' variable
            success = True
    
    return render(request, 'vendor/add_repair.html', {'form': form, 'success':success}) # render the empty form for the user to fill in

# class VendorView(viewsets.ModelViewSet):
#     serializer_class = VendorSerializer
#     queryset = Vendor.objects.all()