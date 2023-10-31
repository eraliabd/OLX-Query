from django.contrib import admin

# Register your models here.
from .models import Category, Ads, Product

admin.site.register(Category)
admin.site.register(Ads)
admin.site.register(Product)
