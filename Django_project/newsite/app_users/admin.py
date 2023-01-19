from django.contrib import admin

from .models import Profile, History, Delivery


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id']


class PayAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Delivery, PayAdmin)

