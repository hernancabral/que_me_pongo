import csv

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
    def get_recommendation(cls, temperature: int, rain: bool, user_bias: int):
        temperature = temperature + user_bias
        head = Clothes.objects.filter(type='head', min_temperature__lte=temperature).order_by('min_temperature').last()
        body = Clothes.objects.filter(type='body', min_temperature__lte=temperature).order_by('min_temperature').last()
        legs = Clothes.objects.filter(type='legs', min_temperature__lte=temperature).order_by('min_temperature').last()

        recommendation = {}
        if head is not None:
            recommendation['head'] = head.description
        else:
            recommendation['head'] = 'No tengo nada para recomendarte'
        if body is not None:
            recommendation['body'] = body.description
        else:
            recommendation['body'] = 'No tengo nada para recomendarte'
        if legs is not None:
            recommendation['legs'] = legs.description
        else:
            recommendation['legs'] = 'No tengo nada para recomendarte'
        if rain:
            recommendation['rain'] = 'Lleva paraguas'
        else:
            recommendation['rain'] = 'No lleves paraguas'

        return recommendation


class Clothes(models.Model):
    description = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')
    min_temperature = models.IntegerField(default=0)

    @classmethod
    def populate_clothes_db(cls):
        with open('utils/clothes_data.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar=';')
            for row in spamreader:
                Clothes.objects.create(description=row[0], type=row[1], min_temperature=row[2])
