from tabnanny import verbose
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') 

    class Meta:
        db_table = 'category'
        verbose_name=  'Категорию'
        verbose_name_plural= 'Категории'

    def __str__(self):
        return self.name
        
class Countries(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Страна', default='Неизвестна')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') 

    class Meta:
        db_table = 'counrty'
        verbose_name=  'Страна'
        verbose_name_plural= 'Страны'
        ordering = ("id",)
    def __str__(self):
        return f'{self.name}'
    
    
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') 
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='machine_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    
    
    country = models.ForeignKey(to=Countries, on_delete=models.CASCADE, verbose_name='Страна')
    year = models.IntegerField(default=0, verbose_name='Год')
    class Meta:
        db_table = 'product'
        verbose_name=  'Станок'
        verbose_name_plural= 'Станки'
        ordering = ("id",)
    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        
        return self.price
    


# Таблица  сервисных работ для станков

class Services(models.Model):
    name = models.CharField(max_length=150, verbose_name='Работа')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') 
    duration = models.PositiveBigIntegerField(default=0, verbose_name='Длительность')
    machine = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Станок')
    
    class Meta:
        db_table = 'service'
        verbose_name=  'Работа'
        verbose_name_plural= 'Работы'
        ordering = ("id",)
    # def __str__(self):
    #     return f'{self.name} Количество - {self.quantity}'
    
    # def display_id(self):
    #     return f"{self.id:05}"
    
    # def sell_price(self):
    #     if self.discount:
    #         return round(self.price - self.price * self.discount / 100, 2)
        
    #     return self.price