import re
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products, Countries, Services
import goods
from goods.utils import q_search

# Create your views here.
def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)


    country = request.GET.get('country', None)

    countries = Countries.objects.all()

    # query - это поисковый запрос    
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        # goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        goods = Products.objects.filter(category__slug=category_slug)


    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    if country and country != "default":
        goods = goods.filter(country__name=country)



    # Фильтрация по году
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    
    if year_min:
        goods = goods.filter(year__gte=year_min)
    if year_max:
        goods = goods.filter(year__lte=year_max)

    # По 3 товара на страницу
    paginator = Paginator(goods, 3)

    # взять первую страницу
    current_page  = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
        'countries': countries,


    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    service = Services.objects.filter(machine=product)

    context = {
        'product': product,
        'services': service,
    }
    return render(request, 'goods/product.html', context)