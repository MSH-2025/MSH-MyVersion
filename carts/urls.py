from django.urls import path
from carts import views

# Вызывать не будем функцию а просто ее зарегаем. также укажем имя, оно необходимо, вдруг мы поменяли PATH
# Так что лучше использовать псевдоним
app_name = 'carts'

urlpatterns = [
     path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
     path('cart_change/<int:product_id>/', views.cart_change, name='cart_change'),
     path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
 ]