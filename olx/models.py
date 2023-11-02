from django.db import models
from django.db.models.functions import Coalesce
from django.db.models import Q


class CategoryManager(models.Manager):
    def counts(self):
        return super().get_queryset().annotate(ads_count=models.Count('ads'))


class Ads(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    objects = CategoryManager()

    def __str__(self):
        return self.title

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.IntegerField()
    view_count = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 1  Category.objects.filter(title__istartswith="m")
# 2 category = Category.objects.all().filter(title__icontains='avto')
# 3 category = Category.objects.all()[5:10]
# 4 Category.objects.all().filter(created__year=2023)
# 5  Category.objects.all().order_by('-updated')
# 6 Category.objects.all().filter(ads__title__icontains='mah')
# 7  Category.objects.filter(product__isnull=False)
# 8  Category.objects.all().filter(Q(created__year=2022)|Q(title__startswith='S'))
# 9  Product.objects.filter(id=1).update(view_count=F('view_count')+1)
# 10 for c in Category.objects.all():
# ...     print(c.title)
# ...     for p in c.ads.all():
# ...             print(p.title)
# 11 Product.objects.aggregate(models.Sum('view_count'))
# 12 Product.objects.aggregate(models.Avg('price'), models.Max('price'), models.Min('price'))
    # {'price__avg': 67500.0, 'price__max': 250000, 'price__min': 5000}

