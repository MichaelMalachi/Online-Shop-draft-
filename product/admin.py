from django.contrib import admin
from product.models import CustomUser123, Products

# Настройка админки для CustomUser123
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Регистрируем модель CustomUser123 в админке
admin.site.register(CustomUser123, CustomUserAdmin)

# Класс админки для Products
class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)

# Регистрируем модель Products
admin.site.register(Products, ProductsAdmin)
