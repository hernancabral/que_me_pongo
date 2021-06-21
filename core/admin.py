from django.contrib import admin
from core.models import UserBias, Clothes


@admin.register(UserBias)
class UserBiasAdmin(admin.ModelAdmin):
    list_display = ['user', 'bias', 'created_at']


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['description', 'type', 'min_temperature']
