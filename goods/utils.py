from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
# Поиск по сайту (поиск товара по названию/описанию/стране)
from goods.models import Products

def q_search(query):
    # Если запрос состоит только из цифр и длина не больше 5, то поиск по ID продукта
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description", "country__name") #вектор поиска по полям name, description и связанному полю country__name
    query = SearchQuery(query)

    # формирование результата с сортировкой по релевантности поиска
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    #совпадения в поле name
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    #совпадения в поле description
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result