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
        last_bias = models.UserBias.get_latest_bias_for_user(request.user.id)
        new_head_bias = last_bias.head_bias + int(bias)
        new_body_bias = last_bias.body_bias + int(bias)
        new_legs_bias = last_bias.legs_bias + int(bias)
        new_bias = models.UserBias(user=request.user, head_bias=new_head_bias, body_bias=new_body_bias, legs_bias=new_legs_bias)
        new_bias.save()
        return render(request, 'core/feedback.html')
