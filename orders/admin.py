from django.contrib import admin
from orders.models import Order, OrderItem, OrderStatus

# Файл для отображения вкладки "Заказы" в панели администратора
# Параметр prepopulated_fields используется в Django Admin для автоматического заполнения полей на основе значений других полей.

@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('status',)}

admin.site.register(Order)
admin.site.register(OrderItem)