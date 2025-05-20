from math import prod
from platform import machine
from django.db import models
from goods.models import Products, Services

from users.models import User


class OrderitemQueryset(models.QuerySet):
    
    def total_duration(self):
        return sum(cart.service_duration() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class OrderStatus(models.Model):
    status = models.CharField(max_length=50,unique=True, verbose_name="Статус заказа", default='New')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'orderstatus'
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статусы Заказа'        
        ordering = ("status",)

    def __str__(self):
        return f'{self.status}'

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    organisation_info = models.TextField(null=True, blank=True, verbose_name="Организация")
    status = models.ForeignKey(to=OrderStatus, on_delete=models.SET_DEFAULT, verbose_name='Статус заказа', default=None)

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    service = models.ForeignKey(to=Services, on_delete=models.SET_DEFAULT, null=True, verbose_name="Работа", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    duration = models.PositiveBigIntegerField(default=0, verbose_name='Длительность')
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата оформления")

    class Meta:
        db_table = "order_item"
        verbose_name = "Заказанное обслуживание"
        verbose_name_plural = "Заказанные обслуживания"

    objects = OrderitemQueryset.as_manager()

    def srvduration(self):
        return self.duration * self.quantity
    
    def machinename(self):
        service = Services.objects.get(name=self.name)
        product = service.machine  
        return product.name
    

    def __str__(self):
        service = Services.objects.get(name=self.name)
        product = service.machine  
        return f"Работа {self.name} | Станок {product.name} | Заказ № {self.order.pk}"
