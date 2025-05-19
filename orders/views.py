from itertools import product
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from carts.models import Cart

from goods.models import Products
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem #, OrderStatus


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            organisation_info=form.cleaned_data['organisation_info'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            service=cart_item.service
                            name=cart_item.service.name
                            duration=cart_item.service.duration
                            quantity=cart_item.quantity

                            OrderItem.objects.create(
                                order=order,
                                # product=product,
                                name=name,
                                duration=duration,
                                quantity=quantity,
                            )

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Machine Service Hub - Оформление заказа',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)