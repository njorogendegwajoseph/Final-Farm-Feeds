from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    WEIGHT = (
        ('5', '5 Kgs'),
        ('50', '50 Kgs'),
        ('10', '10 Kgs'),
        ('20', '20 Kgs'),
        ('70', '70 Kgs'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='produts/%Y/%m/%d', blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    weight = models.CharField(max_length=2, choices=WEIGHT, default=5)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class Distributors(models.Model):
    image = models.ImageField(upload_to='shops/', blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    location = models.CharField(max_length=200)
    contacts = models.CharField(max_length=12)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:distributors', args=[self.id, self.slug])

    class Meta:
        verbose_name_plural = 'Distributors'


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Subscriptions'


class Order(models.Model):
    '''Order model for placing orders, want order to be a list of products, so we use many to many field'''

    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    additional_notes = models.TextField(blank=True)

    def __str__(self):
        return self.product_name


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Us'
