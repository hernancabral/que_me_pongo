from django.db import models
from django.contrib.auth.models import User
from core.utils import fields


class UserBias(models.Model):
    user = fields.OneToOneField(User, related_name='bias', on_delete=models.CASCADE)
    head_bias = models.IntegerField(default=0)
    body_bias = models.IntegerField(default=0)
    legs_bias = models.IntegerField(default=0)

    @classmethod
    def get_or_initialize_bias(cls, user):
        user_bias = user.bias
        if user_bias is None:
            user_bias = cls.objects.create(user=user)
        return user_bias


class Recommendation:
    @classmethod
    def get_recommendation(cls, weather, user_bias):
        pass


class Clothes(models.Model):
    pass
