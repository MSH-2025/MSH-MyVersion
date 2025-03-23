from django.urls import path
from goods import views

# Вызывать не будем функцию а просто ее зарегаем. также укажем имя, оно необходимо, вдруг мы поменяли PATH
# Так что лучше использовать псевдоним
app_name = 'goods'
urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'), # ведет на каталог
    path('product/<slug:product_slug>/', views.product, name='product'),
]