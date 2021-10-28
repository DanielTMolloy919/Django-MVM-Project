from django.urls import path

from . import views

urlpatterns = [
    path('search/',views.search, name='search'),
#   path('', views.autocomplete, name='autocomplete'),
    path('category_list/',views.show_category, name='category_list'),
#   path('<slug:category_slug>/<slug:repair_slug>/', views.repair, name='repair'), # create the url for a detailed repair view from its category and repair url slug
    path('<slug:category_slug>/', views.category, name='category'),
    
]