from urllib import response
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.models import Cart

from goods.models import Products, Services
from django.http import JsonResponse
from carts.utils import get_user_carts


# Create your views here.
# def cart_add(request, product_id):

#     product = Products.objects.get(id=product_id)
    
#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)

#     return redirect(request.META['HTTP_REFERER'])

def cart_add(request):


    service_id = request.POST.get("service_id")

    service = Services.objects.get(id=service_id)
    product = service.machine  

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, service=service, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, service=service,  product=product, quantity=1)


    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)

            
def cart_change(request, product_id):
    ...

def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)