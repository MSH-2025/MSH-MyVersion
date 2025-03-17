from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Обработка запросов на главную страницу сайта
# HttpRequest -> HttpResponse
def index(request):

    context = {
        'title': "Home - Главная",
        'content': "Магазин мебели HOME",

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "Home - О нас",
        'content': "О нас",
        'text_on_page': "Текст почему этот магащин такой классный для людей"

    }
    return render(request, 'main/about.html', context)