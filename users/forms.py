from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

# класс нужен для валидации вводимых данныхы
# форма с моделями, применяет ограничения в моделях, для ссоответсвия с БД
# 
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()