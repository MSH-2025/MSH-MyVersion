from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

# класс нужен для валидации вводимых данных
# форма с моделями, применяет ограничения в моделях, для соответсвия с БД
# 
class UserLoginForm(AuthenticationForm):
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegistrationForm(UserCreationForm):
 
     class Meta:
         model = User
         fields = (
             "first_name",
             "last_name",
             "username",
             "email",
             "password1",
             "password2",
         )
     
     first_name = forms.CharField()
     last_name = forms.CharField()
     username = forms.CharField()
     email = forms.CharField()
     password1 = forms.CharField()
     password2 = forms.CharField()

class ProfileForm(UserChangeForm):
     class Meta:
         model = User
         fields = (
             "image",
             "first_name",
             "last_name",
             "username",
             "email",)
 
     image = forms.ImageField(required=False)
     first_name = forms.CharField()
     last_name = forms.CharField()
     username = forms.CharField()
     email = forms.CharField()