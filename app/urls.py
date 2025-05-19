"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from main import views
from goods import views
from app import settings
from django.conf.urls.static import static

# Определение ссылок на модули преложения (важно для отображения на web-сайте)
urlpatterns = [
    path('admin/', admin.site.urls), #панель администратора
    path('', include('main.urls', namespace='main')),  #главная страница
    path('catalog/', include('goods.urls', namespace='catalog')),    #каталог товаров
    path('user/', include('users.urls', namespace='user')), # профиль пользователя
    path('cart/', include('carts.urls', namespace='cart')),     #корзина
    path('orders/', include('orders.urls', namespace='orders')),    #заказы
    #path('', include('urls')),  # подключаете маршруты своего приложения
]

# Определение ссылок для страниц об ошибках (необходимо для отладки приложения)
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)