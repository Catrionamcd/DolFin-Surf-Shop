"""
    View for the Product App. This includes the view all
    products.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.db.models.functions import Lower
from .models import Product, Category, SubCategory, Brand, ProductComment
from .forms import ProductForm, ProductCommentForm
from checkout.models import OrderLineItem
from django.core.paginator import Paginator


def update_session(request):

    cat_checked = request.POST.getlist('cat_checked[]')
    cat_checked_num = list(map(int, cat_checked))

    cat_indeterminate = request.POST.getlist('cat_indeterminate[]')
    cat_indeterminate_num = list(map(int, cat_indeterminate))

    sub_checked = request.POST.getlist('sub_checked[]')
    sub_checked_num = list(map(int, sub_checked))

    brand_checked = request.POST.getlist('brand_checked[]')
    brand_checked_num = list(map(int, brand_checked))

    gender_checked = request.POST.getlist('gender_checked[]')
    gender_checked_num = list(map(int, gender_checked))

    if request.is_ajax():
        try:
            request.session['cat_checked'] = cat_checked_num
            request.session['cat_indeterminate'] = cat_indeterminate_num
            request.session['sub_checked'] = sub_checked_num
            request.session['brand_checked'] = brand_checked_num
            request.session['gender_checked'] = gender_checked_num
        except KeyError:
            return HttpResponse('Error')
    else:
        raise Http404

    return HttpResponse("Success")


def all_products(request):
    """A view to show all products, including sorting and search queries """

    categories_list = Category.objects.all().annotate(subcat_count=Count('subcategory'))  # noqa
    subcategories_list = SubCategory.objects.all()
    brands = Brand.objects.all()
    genders = Product.gender.field.choices

    cat_checked = request.session.get('cat_checked', [])
    cat_indeterminate = request.session.get('cat_indeterminate', [])
    sub_checked = request.session.get('sub_checked', [])
    brand_checked = request.session.get('brand_checked', [])
    gender_checked = request.session.get('gender_checked', [])

    category_filter = None
    if request.GET:
        if 'category_filter' in request.GET:
            """ if category selected from Home Page """
            category_filter = request.GET['category_filter']
            if category_filter not in cat_checked:
                """ Update menu Checkbox with selected category"""
                cat_checked.append(category_filter)
                cat_checked = list(map(int, cat_checked))
                request.session['cat_checked'] = cat_checked
                """ Check if Category has sub-categories """
                subcats = SubCategory.objects.filter(category=category_filter)
                for subcat in subcats:
                    if subcat.id not in sub_checked:
                        """ update menu checkbox with sub-categories """
                        sub_checked.append(subcat.id)
                sub_checked = list(map(int, sub_checked))
                request.session['sub_checked'] = sub_checked

    # if NO categories, sub-categories, brands,
    # or gender retrieved from session
    if cat_checked == [] and sub_checked == [] and brand_checked == [] and gender_checked == []:  # noqa
        # then select all categories, sub-categories, brands
        # and genders for view (except gift cards)
        cat_checked = list(categories_list.exclude(giftcard_category=True).values_list('id', flat=True))  # noqa
        sub_checked = list(subcategories_list.exclude(category__giftcard_category=True).values_list('id', flat=True))  # noqa
        brand_checked = list(brands.values_list('id', flat=True))
        gender_checked_string = list([gender[0] for gender in genders])
        gender_checked = list(map(int, gender_checked_string))

    # First get full product list and annotate the
    # sale price of each item """
    products = Product.objects.all().exclude(obsolete=True
        ).exclude(Q(has_gender=True), ~Q(gender__in=gender_checked)  # noqa
        ).filter(  # noqa
            Q(category__in=cat_checked) | Q(subcategory__in=sub_checked),
            Q(brand__in=brand_checked) | Q(category__giftcard_category=True)
        ).annotate(order_count=Count('orderlineitem'))

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    product_count = products.count()
    paginator = Paginator(products, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories_list': categories_list,
        'brands': brands,
        'genders': genders,
        'products': page_obj,
        'product_count': product_count,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'cat_checked': cat_checked,
        'cat_indeterminate': cat_indeterminate,
        'sub_checked': sub_checked,
        'brand_checked': brand_checked,
        'gender_checked': gender_checked,
        'is_paginated': True,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # Get Product that was ordered the most while ordering
    # this selected product. First get a list of all Orders
    # that include this selected Product.
    orders_with_this_product = OrderLineItem.objects.filter(product=product_id).values_list('order', flat=True)  # noqa
    # Next get a list of Product Items ordered in all of
    # the Orders retrieved above BUT not giftcards
    all_products_in_these_orders = OrderLineItem.objects.filter(order__in=orders_with_this_product).exclude(product__category__giftcard_category=True).exclude(product__obsolete=True)  # noqa
    # Now Count how many times each product was ordered
    # across all of these Orders
    each_product_count = all_products_in_these_orders.values('product').order_by('product').annotate(num_ordered=Count('product'))  # noqa
    # Finally sequence from largest to smallest count
    each_product_count_desc = each_product_count.all().order_by('-num_ordered')

    freq_bought_together = ""

    # First check if any additional products in the list. Current product
    # plus at least one other. Only interested in highest count so take from
    # start of list
    if len(each_product_count_desc) > 1:
        # First check if current product is at start of list and
        # if it is then take the next one on the list
        if not each_product_count_desc[0]['product'] == product_id:
            # Must have been order at least 3 times with this product
            # to be considered as Frequently Bought Together
            if each_product_count_desc[0]['num_ordered'] > 2:
                freq_bought_together_id = each_product_count_desc[0]['product']
                freq_bought_together = get_object_or_404(Product, pk=freq_bought_together_id)  # noqa
        else:
            if each_product_count_desc[1]['num_ordered'] > 2:
                freq_bought_together_id = each_product_count_desc[1]['product']
                freq_bought_together = get_object_or_404(Product, pk=freq_bought_together_id)  # noqa

    """
        if orders found for this product hide Admin
        product delete option in product page
    """
    product_has_no_orders = True
    if orders_with_this_product:
        product_has_no_orders = False

    """
        If user is logged on - check if they have created a
        comment for this product
    """
    user_product_comment = ""
    if request.user.is_authenticated:
        try:
            user_product_comment = ProductComment.objects.get(product=product_id, author=request.user)  # noqa
        except ProductComment.DoesNotExist:
            user_product_comment = ""

    """ Get all user review for this product """
    product_comments = ProductComment.objects.filter(product=product_id)

    context = {
        'product': product,
        'freq_bought_together': freq_bought_together,
        'product_has_no_orders': product_has_no_orders,
        'user_product_comment': user_product_comment,
        'product_comments': product_comments,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. Please ensure the form is valid.')  # noqa
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_product_comment(request, product_id):

    """ Add a comment to a product """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductCommentForm(request.POST, request.FILES)
        if form.is_valid():
            product_comment = form.save(commit=False)
            product_comment.product = product
            product_comment.author = request.user
            product_comment.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add comment. Please ensure the form is valid.')  # noqa
    else:
        form = ProductCommentForm()

    template = 'products/product_comment.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_product_comment(request, product_id):

    """ Edit a comment on a product """
    product = get_object_or_404(Product, pk=product_id)
    product_comment = get_object_or_404(ProductComment, product=product,
                                        author=request.user)
    print("COMMENT: ", product_comment.author)
    if request.method == 'POST':
        form = ProductCommentForm(request.POST, request.FILES, instance=product_comment)  # noqa
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated comment!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update comment. Please ensure the form is valid.')  # noqa
    else:
        form = ProductCommentForm(instance=product_comment)
        messages.info(request, f'You are editing a comment for {product.name}')

    template = 'products/product_comment.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product_comment(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product_comment = get_object_or_404(ProductComment, product=product.id,
                                        author=request.user)
    product_comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
