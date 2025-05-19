from django.contrib import admin

from users.models import User

# Файл для отображения вкладки "Пользователи" в панели администратора

admin.site.register(User)