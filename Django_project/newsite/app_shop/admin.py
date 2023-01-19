from django.contrib import admin

from .models import Product, Category, Characteristic, Tegs


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TegsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Tegs, TegsAdmin)
