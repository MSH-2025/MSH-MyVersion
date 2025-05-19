#Определение двух пользовательских тегов для Django-шаблонов, которые облегчают работу с категориями и параметрами GET-запроса

from urllib.parse import urlencode
from django import template

from goods.models import Categories

register = template.Library()

#Возвращает все объекты модели Categories
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

#Принимает контекст шаблона, чтобы получить текущие GET-параметры из запроса
@register.simple_tag(takes_context=True)
def change_paramas(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
