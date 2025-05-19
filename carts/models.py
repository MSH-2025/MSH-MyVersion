from django.db import models

# Файл с дополнительными классами для работы с корзиной
# Класс Cart соответсвует таблице в базе данных

from users.models import User
from goods.models import Products, Services

class CartQueryset(models.QuerySet):
    
    def total_duration(self):
        return sum(cart.service_duration() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Товар')

    service = models.ForeignKey(to=Services, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Работы')

    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects= CartQueryset().as_manager()

    def service_duration(self):
        return self.service.duration * self.quantity
    
    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.product.name} | Работы {self.service.name}'
