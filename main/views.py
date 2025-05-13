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
    about_text = """
    
    <h4>О компании:</h4>
    <p>Мы занимаемся ремонтом станков и другого промышленного оборудования и помогаем предприятиям поддерживать работоспособность техники,
    минимизировать простои и повышать эффективность производства.</p>

    <h4>Наши клиенты:</h4>
    <p>Мы сотрудничаем с промышленными предприятиями, использующими различное сложное оборудование.</p>

    <h4>Наша миссия:</h4>
    <p>Обеспечивать надежное и своевременное обслуживание промышленного оборудования, предлагая клиентам современные решения для учета и управления ремонтом.</p>

    <h4>Приложение «Machine Service Hub» позволяет:</h4>
    <ul>
        <li>Систематизировать учет оборудования (по странам-производителям, годам выпуска и маркам)</li>
        <li>Детализировать виды ремонтов, их сроки и стоимость</li>
        <li>Отслеживать историю обслуживания каждого станка или единицы оборудования на вашем предприятии</li>
        <li>Автоматизировать процессы взаимодействия с предприятиями, позволяя сделать процесс оформления заказов удобнее и быстрее, чем по телефону или при личной встрече</li>
    </ul>

    <p>Machine Service Hub - ваш надежный партнер в ремонте и обслуживании промышленного оборудования!</p>
    """
    
    context = {
        'title': "Machine Service Hub",
        'text_on_page': about_text,
        'safe': True  
    }
    return render(request, 'main/about.html', context)


def contact(request):
    contact_text = """

    <h3>Контакты</h3>
    <p> <p>

    <h4>Главный офис:</h4>
    <p>г. Пермь, ул. Ленина, д. 17, офис 305</p>
    <p>Часы работы: Пн - Пт: 09:00 - 18:00 (по местному времени)</p>

    <h4>Телефоны:</h4>
    <ul>
        <li>Бесплатный по России: 8 (800) 456-78-99</li>
        <li>Мобильный (WhatsApp/Telegram): +7 (912) 555-66-77</li>
        <li>Городской: +7 (342) 123-45-67</li>
    </ul>

    <h4>Электронная почта:</h4>
    <ul>
        <li>Общие вопросы: <a href="mailto:info@machineservicehub.ru">info@machineservicehub.ru</a></li>
        <li>Техподдержка приложения: <a href="mailto:support@machineservicehub.ru">support@machineservicehub.ru</a></li>
    </ul>
    """
    
    context = {
        #'title': "Machine Service Hub",
        'text_on_page': contact_text,
        'safe': True  
    }
    return render(request, 'main/about.html', context)



def delivery(request):
    delivery_text = """

    <h4>Способы доставки</h4>
    <p> <p>
    
    <ul>
    <li>Курьерская доставка</li>
    <p>Быстрая отправка заказов через СДЭК, DHL, Boxberry и другие транспортные компании.  Сроки: 1–7 дней (в зависимости от региона)</p>
    
    <li>Транспортными компаниями</li>
    <p>Доставка крупногабаритного оборудования и станков через ПЭК, Деловые Линии, ЖД-перевозки.  Рассчитывается индивидуально</p>
    </ul>
    
    <h4>Способы оплаты</h4>

    <ul>
    <li>Безналичный расчет</li>
    <p>Оплата по счету для юридических лиц и ИП (с НДС или без).</p>
    
    <li>Наличные</li>
    <p>Оплата на месте при самовывозе</p>
    </ul>
    
    <h4>Гарантии и возврат</h4>
    
    <ul>
    <li>Контроль качества – все детали и оборудование проверяются перед отправкой.</li>
    <li>Возврат и обмен – в течение 14 дней при наличии заводского брака (согласно законодательству РФ).</li>
    </ul>
    """
    
    context = {
        #'title': "Machine Service Hub",
        'text_on_page': delivery_text,
        'safe': True  
    }
    return render(request, 'main/about.html', context)