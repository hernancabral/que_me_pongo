from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from weather.service import WeatherService
from core import models


class IndexView(View):

    def get(self, request):
        return render(request, 'registration/login.html')


class DashboardView(View):

    def get(self, request):
        today_weather = WeatherService.get_weather()
        user_bias = models.UserBias.get_or_initialize_bias(request.user)
        recommended_clothes = models.Recommendation.get_recommendation(int(today_weather['temperature']),
                                                                       today_weather['rain'], user_bias.bias)
        context = {'temperature': int(today_weather['temperature']),
                   'head': recommended_clothes['head'],
                   'body': recommended_clothes['body'],
                   'legs': recommended_clothes['legs'],
                   'feet': recommended_clothes['feet'],
                   'rain': recommended_clothes['rain']
                   }
        return render(request, 'core/dashboard.html', context)


class FeedbackView(View):
    def post(self, request):
        bias = request.POST['feedback']
        modifier = request.POST['weather_accuracy']
        last_bias = models.UserBias.get_latest_bias_for_user(request.user.id)
        bias = float(bias) * float(modifier)
        new_bias = last_bias.bias + int(bias)
        new_user_bias = models.UserBias(user=request.user, bias=int(new_bias))
        new_user_bias.save()
        return render(request, 'core/feedback.html')
