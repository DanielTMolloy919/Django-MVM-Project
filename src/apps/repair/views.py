import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Category, Repair

from .filters import RepairFilter # import the filter for the search view

def is_valid_query(query): # checks that a query actually contains data
    valid_bool = query != '' and query is not None
    return valid_bool

def search(request):
    qs = Repair.objects.all()

    category_query = request.GET.get('category')
    repair_type_query = request.GET.get('repair_type')
    location_query = request.GET.get('location')

    sort_by_query = request.GET.get('sort_by')

    if is_valid_query(category_query): # filter based on category search
        qs = qs.filter(category__name__icontains=category_query) 
    else:
        category_query = ""

    if is_valid_query(repair_type_query): #filter based on repair type
        qs = qs.filter(repair_type__name__icontains=repair_type_query)
    else:
        repair_type_query = ""
        
    if is_valid_query(sort_by_query):
        if sort_by_query == "cheapest":
            qs = qs.order_by('price')
        elif sort_by_query == "highest_rated":
            qs = qs.order_by('-vendor__g_rating')
    else:
        sort_by_query = ""

    sort_list = { # a dictionary of different ways the results can be sorted
        'best':'Best',
        'highest_rated':'Highest Rated',
        'cheapest':'Cheapest'
    }

    context = {
        'queryset': qs,
        'category_query': category_query,
        'repair_type_query': repair_type_query,
        'sort_by_query': sort_by_query,
        'sort_list': sort_list
    }

    return render(request, 'repair/search.html', context)
    
def repair(request, category_slug, repair_slug):
    repair = get_object_or_404(Repair, category__slug=category_slug, slug=repair_slug)

    similar_repairs = list(repair.category.repairs.exclude(id=repair.id))

    if len(similar_repairs) >= 4:
        similar_repairs = random.sample(similar_repairs, 4)

    return render(request, 'repair/repair.html', {'repair': repair, 'similar_repairs': similar_repairs})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'repair/category.html', {'category': category}) 

def show_category(request): # very lightweight category viewer
    return render(request, "repair/category_list.html", {'category': Category.objects.all()})