"""
    Models for the Product App. This includes the Category Model,
    the Brand Model, the Colour Model, the Product Model and 
    the Product Inventory Model
"""

from django.db import models


class Category(models.Model):
    """
        The Category Model will hold all categories of Products
        sold on the DolFin Surf Shop, such as swimwear, wetsuits,
        etc. It will hold an image for the category and a integer
        for sales percentage discount for each category. It will also
        hold a boolean field for giftcard category.
    """
    class Meta:
        """
            Make Categories more readable on Admin Dashboard
        """
        verbose_name_plural = 'Categories'

    category_name_slug = models.CharField(max_length=50, unique=True)
    category_name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    sale_percent = models.IntegerField(null=False, blank=False, default=0)
    giftcard_category = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    """
        The Brand Model will hold all the different brand names
    """
    brand_name_slug = models.SlugField(max_length=50, unique=True)
    brand_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.brand_name


class Colour(models.Model):
    """
        The Colour Model will hold the different colours for different
        products.
    """

    colour_slug = models.SlugField(max_length=50, unique=True)
    colour = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.colour


class Product(models.Model):
    """
        The Product Model will hold the Product details
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_gender = models.BooleanField(default=False, null=True, blank=True)
    has_colours = models.BooleanField(default=False, null=True, blank=True)
    has_length = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    obsolete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    """
        The Product Inventory Model will hold the quantity of each product
        available in stock.
    """

    class Meta:
        """
            Make Product Inventory more readable on Admin Dashboard
        """
        verbose_name_plural = 'Product Inventory'

    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.SET_NULL)
    colour = models.ForeignKey('Colour', null=True, blank=True,
                               on_delete=models.SET_NULL)
    XTRASMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XTRALARGE = 'XL'
    SIZE_CHOICES = [
        (XTRASMALL, 'XSmall'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XTRALARGE, 'XLarge'),
    ]
    size = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=SIZE_CHOICES,
    )
    MALE = 'M'
    FEMALE = 'F'
    JMALE = 'JM'
    JFEMALE = 'JF'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (JMALE, 'Junior Male'),
        (JFEMALE, 'Junior Female'),
    ]
    gender = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=GENDER_CHOICES,
    )
    SHORT = 'S'
    MID = 'M'
    LONG = 'L'
    LENGTH_CHOICES = [
        (SHORT, 'Short'),
        (MID, 'Mid-Length'),
        (LONG, 'Long'),
    ]
    length = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=LENGTH_CHOICES,
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f'Product: {self.product}, Colour: {self.colour}, \
            Size: {self.size}, Gender: {self.gender}, Length: {self.length},\
            Quantity: {self.quantity}'