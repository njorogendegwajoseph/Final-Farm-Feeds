from django.conf import settings
from twilio.rest import Client
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Distributors
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from .forms import SubscriptionForm


# Create your views here.

def home(request):
    return render(request, 'shop/product/homepage.html')


def team(request):
    return render(request, 'shop/product/team.html')


def about(request):
    return render(request, 'shop/product/about.html')


def production(request):
    return render(request, 'shop/product/production.html')


def product_list(request, category_slug=None):
    top_products = Product.objects.all()[:6]
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/list.html', {'categories': categories, 'category': category, 'products': products, 'page': page, 'top_products': top_products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def distributors(request):
    distributors = Distributors.objects.all()
    paginator = Paginator(distributors, 10)
    page = request.GET.get('page')
    try:
        distributors = paginator.page(page)

    except PageNotAnInteger:
        distributors = paginator.page(1)
    except EmptyPage:
        distributors = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/distributors.html', {'distributors': distributors})


def filter_distributors_by_location(request):
    location = request.GET.get('location')

    if location:
        distributors = Distributors.objects.filter(
            location__icontains=location)
    else:
        distributors = Distributors.objects.all()

    paginator = Paginator(distributors, 10)
    page = request.GET.get('page')

    try:
        distributors = paginator.page(page)
    except PageNotAnInteger:
        distributors = paginator.page(1)
    except EmptyPage:
        distributors = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/distributors.html', {'distributors': distributors})


def filter_products_by_name(request):
    name = request.GET.get('name')
    if name:
        products = Product.objects.filter(name__icontains=name)

    else:
        products = Product.objects.all()

    paginator = Paginator(products, 6)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/list.html', {'products': products})


def show_map(request):
    # Sample latitude and longitude (replace with your own data)
    latitude = 37.7749
    longitude = -122.4194

    context = {
        'latitude': latitude,
        'longitude': longitude,
    }

    return render(request, 'shop/product/map.html', context)


def send_whatsapp_message(to, body):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_='whatsapp:YOUR_TWILIO_WHATSAPP_NUMBER',
        body=body,
        to='whatsapp:' + to
    )


def subscribe(request):
    '''a function to subscribe to the newsletter and print a message to the user and redirect to the home page'''
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been subscribed successfully')

    else:
        form = SubscriptionForm()

    return render(request, 'shop:distributors', {'form': form})
