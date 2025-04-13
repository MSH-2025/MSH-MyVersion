from django.shortcuts import redirect, render
from carts.models import Cart

from goods.models import Products, Services

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

def cart_add(request, service_id):

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

    return redirect(request.META['HTTP_REFERER'])

            
def cart_change(request, product_id):
    ...

# def cart_remove(request, cart_id) :
#     cart = Cart.objects.get()
#     return redirect(request.META['HTTP_REFERER'])