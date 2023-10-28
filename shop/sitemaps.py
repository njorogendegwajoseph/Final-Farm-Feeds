from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Product.objects.all()
    
    def lastmod(self, obj):
        return obj.updated