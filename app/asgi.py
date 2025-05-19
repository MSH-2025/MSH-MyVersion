"""
Конфигурация ASGI для проекта (ASGI - клиент-серверный протокол взаимодействия веб-сервера и приложения)
Файл раскрывает вызываемый ASGI как переменную уровня модуля с именем ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
