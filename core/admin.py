from django.contrib import admin
from core.models import UserBias


@admin.register(UserBias)
class UserBiasAdmin(admin.ModelAdmin):
    list_display = ['user', 'head_bias', 'body_bias', 'legs_bias']
