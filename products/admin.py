"""
    Admin for the models in the Product App. This includes the
    Category Model, the Brand Model, the Colour Model, the
    Product Model and the Product Inventory Model.
"""

from django.contrib import admin
from .models import Category, Brand, Colour
from .models import Product, ProductInventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
        Admin for the for the Category Model.
    """
    prepopulated_fields = {'category_name_slug': ('category_name',)}
    fields = ('category_name', 'category_name_slug', 'sale_percent',
              'giftcard_category')
    list_display = (
        'category_name',
        'category_name_slug',
        'sale_percent',
        'giftcard_category'
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
        Admin for the for the Brand Model.
    """
    prepopulated_fields = {'brand_name_slug': ('brand_name',)}
    fields = ('brand_name', 'brand_name_slug')
    list_display = (
        'brand_name',
        'brand_name_slug'
    )


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    """
        Admin for the for the Colour Model.
    """
    prepopulated_fields = {'colour_slug': ('colour',)}
    fields = ('colour', 'colour_slug')
    list_display = (
        'colour',
        'colour_slug'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
        Admin for the for the Product Model.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'date_created'
    )

    ordering = ('sku',)


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    """
        Admin for the for the Product Inventory Model.
    """
    list_display = (
        'product',
        'colour',
        'size',
        'gender',
        'length',
        'quantity'
    )


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Brand, BrandAdmin)
# admin.site.register(Colour, ColourAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductInventory, ProductInventoryAdmin)