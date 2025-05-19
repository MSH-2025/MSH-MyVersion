from django.contrib import admin
from orders.models import Order, OrderItem, OrderStatus

# Register your models here.
@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('status',)}

admin.site.register(Order)
admin.site.register(OrderItem)