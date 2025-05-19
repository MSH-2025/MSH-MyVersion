from django.urls import path
from goods import views

# Ссылки на страницы различных действий с корзиной (отображение у пользователя)
app_name = 'goods'
urlpatterns = [
    path('search/', view=views.catalog, name='search'), # поиск
    path('<slug:category_slug>/', views.catalog, name='index'), # каталог
    path('product/<slug:product_slug>/', views.product, name='product'), #товар (станок/оборудование и перечень возможных работ)
]