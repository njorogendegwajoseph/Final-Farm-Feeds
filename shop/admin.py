from django.contrib import admin
from .models import Category, Product, Distributors, Subscription
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'weight']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Distributors)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    list_filter = ['location']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subscription)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = [ 'email']