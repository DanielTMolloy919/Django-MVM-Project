from django.urls import path

from . import views

urlpatterns = [
    path('search/',views.search, name='search'),
    path('category_list/',views.show_category, name='category_list'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'), # create the url for a detailed product view from its category and product url slug
    path('<slug:category_slug>/', views.category, name='category'),
    
]