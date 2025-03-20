from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from goods.models import Categories

#Обработка запросов на главную страницу сайта
# HttpRequest -> HttpResponse
def index(request):
    categories = Categories.objects.all()
    context = {
        'title': "Home - Главная",
        'content': "Магазин мебели HOME",
        'categories': categories

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "Home - О нас",
        'content': "О нас",
        'text_on_page': "Текст почему этот магащин такой классный для людей"

    }
    return render(request, 'main/about.html', context)