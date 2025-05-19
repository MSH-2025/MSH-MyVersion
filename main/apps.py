from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

#Переопределение класса для Axes (был по умолчанию на английском языке)
class AxesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "axes"
    verbose_name = "Контроль доступа"
