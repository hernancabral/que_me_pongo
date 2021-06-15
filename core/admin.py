from django.contrib import admin
from core.models import UserBias


@admin.register(UserBias)
class UserBiasAdmin(admin.ModelAdmin):
    list_display = ['user', 'bias', 'created_at']
