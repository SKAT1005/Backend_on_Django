from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=1024, verbose_name='Название товара')
    photo = models.ImageField(upload_to='prod/', verbose_name='Аватарка')
    description = models.CharField(max_length=1024, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена товара')
    manufacturer = models.CharField(max_length=256, verbose_name='Производитель')
    limited_edition = models.BooleanField(default=False, verbose_name='Эксклюзивность товара')
    category = models.ManyToManyField('Category', verbose_name='Категории')
    characteristics = models.ManyToManyField('Characteristic', verbose_name='Характеристики', related_name='char')
    reviews = models.ManyToManyField('Reviews', verbose_name='Отзывы', related_name='reviews', blank=True)
    tegs = models.ManyToManyField('Tegs', verbose_name='Тэги', related_name='tegs')
    reviews_count = models.IntegerField(default=0)
    count = models.IntegerField(default=0, verbose_name='Счетчик проданных товаров')

    def short_description(self):
        return self.description[:50]


class Reviews(models.Model):
    user_name = models.CharField(max_length=512, verbose_name='Имя комментатора')
    avatar = models.ImageField(upload_to='files/', verbose_name='Аватарка', blank=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации отзыва')
    text = models.CharField(max_length=4096, verbose_name='Текст отзыва')


class Category(models.Model):
    min_price = models.FloatField(verbose_name='минимальная цена в категории', default=0)
    image = models.ImageField(upload_to='prod/', verbose_name='Иконка категории', null=False)
    name = models.CharField(max_length=128, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название характеристики')
    value = models.CharField(max_length=512, verbose_name='Значение характеристики')
    def __str__(self):
        return self.name


class Tegs(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название тега')

    def __str__(self):
        return self.name
