"""
    Models for the Product App. This includes the Category Model,
    the Brand Model the Product Model and the Product Inventory Model
"""

from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    category_name_slug = models.CharField(max_length=50, unique=True)
    category_name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    sale_percent = models.IntegerField(null=False, blank=False, default=0)
    giftcard_category = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.category_name


class Brand(models.Model):

    brand_name_slug = models.SlugField(max_length=50, unique=True)
    brand_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.brand_name


class Colour(models.Model):

    colour_slug = models.SlugField(max_length=50, unique=True)
    colour = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.colour


class Product(models.Model):
    category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=False, blank=False, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_gender = models.BooleanField(default=False, null=True, blank=True)
    has_colours = models.BooleanField(default=False, null=True, blank=True)
    has_length = models.BooleanField(default=False, null= True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    obsolete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey('Colour', null=True, blank=True, on_delete=models.SET_NULL)
    size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    gender = models.CharField(max_length=2, null=True, blank=True) # M, F, JM, JF
    length = models.CharField(max_length=2, null=True, blank=True) # L, M, S
    quantity = models.IntegerField(null=False, blank=False, default=0)


    def __str__(self):
        return f'Product: {self.product}, Colour: {self.colour}, \
            Size: {self.size}, Gender: {self.gender}, Length: {self.length},\
            Quantity: {self.quantity}'

