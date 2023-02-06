from django.contrib.auth.models import User
from django.db import models

from app_shop.models import Product, Category


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='users')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True)
    avatar = models.ImageField(upload_to='files/', verbose_name='Аватарка', blank=True)
    cart = models.ManyToManyField(Product, blank=True, related_name='product', verbose_name='Корзина')
    selected_category = models.ManyToManyField(Category, blank=True, related_name='sel_cat',
                                               verbose_name='Избранные категории')
    history = models.ManyToManyField('History', blank=True, related_name='history', verbose_name='История заказов')
    city = models.CharField(max_length=256, blank=True, verbose_name='Город')
    address = models.CharField(max_length=1024, blank=True, verbose_name='Адрес')
    historys_count = models.IntegerField(default=0, name='Кол-во историй')

    @property
    def total_price(self):
        queryset = self.cart.all().aggregate(
            total_price=models.Sum('price'))
        return float(queryset["total_price"])


class History(models.Model):
    number_history = models.IntegerField(default=1, name='id истории')
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    prods = models.ManyToManyField(Product, blank=True, related_name='prod', verbose_name='Продукты')
    total_price = models.IntegerField(default=0, blank=True, verbose_name='Общая стоимость')
    type_of_delivery = models.CharField(max_length=32, verbose_name='Тип доставки')
    type_of_pay = models.CharField(max_length=64, verbose_name='Тип оплаты')
    status = models.CharField(max_length=16, verbose_name='Статус оплаты')
    error = models.CharField(max_length=256, blank=True, verbose_name='Ошибка')
    pub_date = models.DateField(auto_now_add=True)


class Delivery(models.Model):
    name = models.CharField(max_length=32)
    express_delivery = models.FloatField(verbose_name='Экспресс доставка, стоимость')
    delivery = models.FloatField(verbose_name='Обычная доставка, стоимость')
    min_cart = models.FloatField(verbose_name='Минимальная стоимость для бесплатной доставки')

    def __str__(self):
        return self.name
