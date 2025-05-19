from django.contrib import admin

# Файл для отображения раздела "Товары" в панели администратора
# Параметр prepopulated_fields используется в Django Admin для автоматического заполнения полей на основе значений других полей.

from goods.models import Categories, Products, Countries, Services

@admin.register(Categories) #вкладка "категории" в разделе "товары"
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)   #вкладка "Станки" в разделе "товары"
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Countries)  #вкладка "Страны" в разделе "товары"
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Services)   #вкладка "Работы" в разделе "товары"
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}