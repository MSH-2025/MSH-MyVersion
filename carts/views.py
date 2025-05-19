from urllib import response
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.models import Cart

from goods.models import Products, Services
from django.http import JsonResponse
from carts.utils import get_user_carts

from django.contrib import messages

''' Здесь и далее под товаром понимается работа с конкретным станком/оборудованием,
    которую клиент хочет в будущем заказать у предприятия, выполняющего ремонт '''

# Добавление товара в корзину
def cart_add(request):


    service_id = request.POST.get("service_id")

    service = Services.objects.get(id=service_id) # Работа
    product = service.machine  # Станок

    # Если пользователь авторизован, выполняется действие
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, service=service, product=product) 

        if carts.exists(): # Уже есть товары в корзине, т.е. "корзина создана"
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        # Товары в корзину не добавлены
        else:   
            Cart.objects.create(user=request.user, service=service,  product=product, quantity=1)

    # Если нет - уведомление о необходимости авторизации
    if not request.user.is_authenticated:
        return JsonResponse({
            "error": "auth_required",
            "message": "Для добавления товара в корзину необходимо войти или зарегистрироваться."
        }, status=401)

    user_cart = get_user_carts(request) #функция, которая возвращает список корзин пользователя
    
    # Отображение товаров, добавленных в корзины с сортировкой по дате-времени добавления
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart.order_by('created_timestamp')}, request=request)

    # Уведомление + ссылка на страницу корзины как результат функции
    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)

# Изменение количества товаров в корзине
def cart_change(request):
     cart_id = request.POST.get("cart_id") #Идентификатор корзины
     quantity = request.POST.get("quantity") # Кол-во товаров в корзине
 
     cart = Cart.objects.get(id=cart_id)
 
     cart.quantity = quantity
     cart.save()
     updated_quantity = cart.quantity
 
     cart = get_user_carts(request)
     # Отображение товаров, добавленных в корзины с сортировкой по дате-времени добавления
     cart_items_html = render_to_string(
         "carts/includes/included_cart.html", {"carts": cart.order_by('created_timestamp')}, request=request)
 
    # Уведомление + ссылка на изменную страницу корзины как результат функции
     response_data = {
         "message": "Количество изменено",
         "cart_items_html": cart_items_html,
         "quantity": quantity,
     }
 
     return JsonResponse(response_data)

# Изменение товаров из корзины
def cart_remove(request):
    
    cart_id = request.POST.get("cart_id") #Идентификатор корзины

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    # Отображение товаров, добавленных в корзины с сортировкой по дате-времени добавления
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    # Уведомление + ссылка на изменную страницу корзины как результат функции
    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)