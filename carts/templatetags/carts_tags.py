import re
from django import template

from carts.models import Cart
from carts.utils import get_user_carts

# Определяете простой тег user_carts, который принимает объект request и возвращает результат функции get_user_carts(request
# get_user_carts - это функция, которая возвращает данные о корзине пользователя на основе запроса request

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)