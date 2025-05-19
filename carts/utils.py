from carts.models import Cart


def get_user_carts(request):
    #Только для авторизованных пользователей
    if request.user.is_authenticated:
        # Можно посмотреть, какие товары добавлены в корзину
        return Cart.objects.filter(user=request.user)