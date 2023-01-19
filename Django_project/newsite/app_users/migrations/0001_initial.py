# Generated by Django 4.1.5 on 2023-02-01 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('express_delivery', models.FloatField(verbose_name='Экспресс доставка, стоимость')),
                ('delivery', models.FloatField(verbose_name='Обычная доставка, стоимость')),
                ('min_cart', models.FloatField(verbose_name='Минимальная стоимость для бесплатной доставки')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id истории', models.IntegerField(default=1)),
                ('total_price', models.IntegerField(blank=True, default=0, verbose_name='Общая стоимость')),
                ('type_of_delivery', models.CharField(max_length=32, verbose_name='Тип доставки')),
                ('type_of_pay', models.CharField(max_length=32, verbose_name='Тип оплаты')),
                ('status', models.CharField(max_length=16, verbose_name='Статус оплаты')),
                ('error', models.CharField(blank=True, max_length=256, verbose_name='Ошибка')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('prods', models.ManyToManyField(blank=True, related_name='prod', to='app_shop.product', verbose_name='Продукты')),
            ],
        ),
        migrations.CreateModel(
            name='TypePay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('avatar', models.ImageField(blank=True, upload_to='files/', verbose_name='Аватарка')),
                ('city', models.CharField(blank=True, max_length=256, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=1024, verbose_name='Адрес')),
                ('id истории для повторной оплаты', models.IntegerField(default=0)),
                ('Кол-во историй', models.IntegerField(default=0)),
                ('cart', models.ManyToManyField(blank=True, related_name='product', to='app_shop.product', verbose_name='Корзина')),
                ('history', models.ManyToManyField(blank=True, related_name='history', to='app_users.history', verbose_name='История заказов')),
                ('selected_category', models.ManyToManyField(blank=True, related_name='sel_cat', to='app_shop.category', verbose_name='Избранные категории')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='app_users.profile', verbose_name='Пользователь'),
        ),
    ]