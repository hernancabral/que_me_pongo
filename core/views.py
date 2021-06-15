from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from weather.service import WeatherService
from core import models


class IndexView(View):

    # TODO: login page
    def get(self, request):
        return render(request, 'registration/login.html')


class DashboardView(View):

    def get(self, request):
        today_weather = WeatherService.get_weather()
        user_bias = models.UserBias.get_or_initialize_bias(request.user)
        recommended_clothes = models.Recommendation.get_recommendation(today_weather, user_bias)
        context = {'temperature': '10', 'head': 'gorro', 'body': 'campera', 'legs': 'jeans'}
        return render(request, 'core/dashboard.html', context)


class FeedbackView(View):
    # TODO: feedback form
    def post(self, request):
        bias = request.POST['feedback']
        modifier = request.POST['weather_accuracy']
        last_bias = models.UserBias.get_latest_bias_for_user(request.user.id)
        bias = bias * int(modifier)
        new_bias = last_bias.bias + int(bias)
        new_user_bias = models.UserBias(user=request.user, bias=new_bias)
        new_user_bias.save()
        return render(request, 'core/feedback.html')
