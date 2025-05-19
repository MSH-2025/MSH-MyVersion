"""
Конфигурация WSGI для проекта (WSGI - клиент-серверный протокол взаимодействия веб-сервера и приложения)
Файл раскрывает вызываемый WSGI как переменную уровня модуля с именем ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()
