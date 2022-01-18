from django.shortcuts import render
from products.models import Category

# View to render the index page.


def index(request):
    """A view to return the index page"""

    categories = Category.objects.all().order_by('giftcard_category')

    """ First check if any Sales in place """
    sale_in_progress = ""
    sale_categories = Category.objects.filter(sale_percent__gt=0)
    if len(sale_categories)>0:
        sale_in_progress = True

    context = {
        'categories': categories,
        'sale_in_progress': sale_in_progress,
    }

    return render(request, 'home/index.html', context)


