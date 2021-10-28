from django.shortcuts import render

from apps.repair.models import Repair

def frontpage(request):
    newest_repairs = Repair.objects.all()[0:8]
    return render(request,"core/frontpage.html", {'newest_repairs': newest_repairs})

def contact(request):
    return render(request,"core/contact.html")