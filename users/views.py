from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Prefetch
from django.utils import timezone

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from orders.models import Order, OrderItem

# Create your views here.


def login(request):
    login_attempts = request.session.get('login_attempts', 0)

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            request.session['login_attempts'] = 0  # сброс попыток
            messages.success(request, f"{username}, Вы вошли в аккаунт")
            return redirect('main:index')
        else:
            login_attempts += 1
            request.session['login_attempts'] = login_attempts
            messages.warning(request, "Неверный логин или пароль.")

    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form,
    }

    if login_attempts >= 5:
        messages.error(request, "Превышено количество попыток входа.")
        return redirect('main:index')

    return render(request, 'users/login.html', context)


def registration(request):
     if request.method == 'POST':
         form = UserRegistrationForm(data=request.POST)
         if form.is_valid():
             form.save()
             user = form.instance
             user.backend = 'django.contrib.auth.backends.ModelBackend'
             auth.login(request, user)
             messages.success(request, f"{user.username}, Вы зарегистрировались и вошли в аккаунт")
             return HttpResponseRedirect(reverse('main:index'))
     else:
         form = UserRegistrationForm()
     
     context = {
         'title': 'Home - Регистрация',
         'form': form
     }
     return render(request, 'users/registration.html', context)

# def profile(request):
#     context = {
#         'title': 'Home - Кабинет'
#     }
#     return render(request, 'users/profile.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("service"),
                )
            ).order_by("-id")
    
    context = {
        'title': 'Home - Кабинет',
        'form': form,
        'orders': orders,
        
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')

# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Чтобы не выкидывало из сессии
#             # Перенаправление или сообщение об успехе
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', context})