from django.contrib import admin
from .models import Category, Product, Distributors, Subscription, Order, ContactUs
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
    list_display = ['name', 'location', 'active']
    list_filter = ['location', 'active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subscription)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'quantity', 'customer_name',
                    'contact_number', 'email', 'additional_notes']
    list_filter = ['product_name', 'customer_name', 'contact_number', 'email']
    list_editable = ['quantity']
    prepopulated_fields = {'product_name': ('product_name',)}


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ['name', 'email', 'subject']
    prepopulated_fields = {'subject': ('subject',)}
