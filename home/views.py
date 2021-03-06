from django.shortcuts import render
from products.models import Category, Brand, Product
from django.db.models import Count

# View to render the index page.


def index(request):
    """A view to return the index page"""

    categories = Category.objects.all().order_by('giftcard_category')
    categories_list = Category.objects.all().annotate(subcat_count=Count('subcategory'))  # noqa
    brands = Brand.objects.all()
    genders = Product.gender.field.choices

    # On home page so update menu to turn off all
    # category/sub-category checkboxes and turn on all others
    cat_checked = []
    cat_indeterminate = []
    sub_checked = []
    brand_checked = list(brands.values_list('id', flat=True))
    gender_checked_string = list([gender[0] for gender in genders])
    gender_checked = list(map(int, gender_checked_string))

    """ Also update these settings to the session storage"""
    request.session['cat_checked'] = cat_checked
    request.session['cat_indeterminate'] = cat_indeterminate
    request.session['sub_checked'] = sub_checked
    request.session['brand_checked'] = brand_checked
    request.session['gender_checked'] = gender_checked

    """ Check if any Sales in place """
    sale_in_progress = ""
    sale_categories = Category.objects.filter(sale_percent__gt=0)
    if len(sale_categories) > 0:
        sale_in_progress = True

    context = {
        'categories': categories,
        'sale_in_progress': sale_in_progress,
        'categories_list': categories_list,
        'brands': brands,
        'genders': genders,
        'cat_checked': cat_checked,
        'cat_indeterminate': cat_indeterminate,
        'sub_checked': sub_checked,
        'brand_checked': brand_checked,
        'gender_checked': gender_checked,
    }

    return render(request, 'home/index.html', context)
