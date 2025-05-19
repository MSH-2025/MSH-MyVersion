from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

class AxesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "axes"
    verbose_name = "Контроль доступа"
