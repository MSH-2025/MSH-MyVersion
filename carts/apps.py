from django.apps import AppConfig

# Инициализация модуля "carts"

class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'
    verbose_name = "Корзины"
