from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from goods.models import Categories

#Обработка запросов на главную страницу сайта
# HttpRequest -> HttpResponse
def index(request):
    context = {
        'title': "Machine Service Hub - Главная",
        'content': "Магазин станков Machine Service Hub",
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "Machine Service Hu - О нас",
        'content': "О нас",
        'text_on_page': "Умный текст"

    }
    return render(request, 'main/about.html', context)