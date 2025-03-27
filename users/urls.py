from django.urls import path
from users import views

# Вызывать не будем функцию а просто ее зарегаем. также укажем имя, оно необходимо, вдруг мы поменяли PATH
# Так что лучше использовать псевдоним
app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]