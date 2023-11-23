from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('ditributors/', views.distributors, name='distributors'),
    path('ditributors/filtered/',
         views.filter_distributors_by_location, name='filtered'),
    path('products/filtered/', views.filter_products_by_name,
         name='filtered_products'),
    path('about/', views.about, name='about'),
    path('tag/<slug:tag_slug>/', views.distributors, name='post_list_by_tag'),
    path('map/', views.show_map, name='map'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('team/', views.team, name='team'),
    path('order/', views.create_order, name='create_order'),
    path('contact/', views.contactus, name='contactus'),





]
