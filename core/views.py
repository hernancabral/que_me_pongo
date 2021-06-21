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
                   'bias': int(user_bias.bias + int(today_weather['temperature'])),
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
        if modifier == 'OK':
            bias = float(bias)
        elif modifier == 'True': #mas calor
            if bias == '2': #calor
                bias = float(bias) * -0.5
            elif bias == '-2': #frio
                bias = float(bias) * 1.5
            elif bias == '0':
                bias = float(bias) + 1
        elif modifier == 'False': #mas frio
            if bias == '2': #calor
                bias = float(bias) * 1.5
            elif bias == '-2': #frio
                bias = float(bias) * 0.5
            elif bias == '0':
                bias = float(bias) - 1
        last_bias = models.UserBias.get_latest_bias_for_user(request.user.id)
        new_bias = last_bias.bias + bias
        new_user_bias = models.UserBias(user=request.user, bias=int(new_bias))
        new_user_bias.save()
        return render(request, 'core/feedback.html')
