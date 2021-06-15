from django.db import models
from django.contrib.auth.models import User


class UserBias(models.Model):
    user = models.ForeignKey(User, related_name='bias', on_delete=models.CASCADE)
    bias = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_latest_bias_for_user(cls, user_id):
        qs = cls.objects.filter(user=user_id)
        return qs.order_by('created_at').last()

    @classmethod
    def get_or_initialize_bias(cls, user):
        user_bias = cls.get_latest_bias_for_user(user.id)
        if user_bias is None:
            user_bias = cls.objects.create(user=user)
        return user_bias


class Recommendation:
    @classmethod
    # TODO: add recommendation engine
    def get_recommendation(cls, weather, user_bias):
        pass


class Clothes(models.Model):
    pass
