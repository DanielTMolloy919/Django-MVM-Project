import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Category, Repair

from .filters import RepairFilter # import the filter for the search view

def search(request):
    
    repairFilter = RepairFilter(request.GET, queryset=Repair.objects.all())

    return render(request, 'repair/search.html', {'filter': repairFilter})
    
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