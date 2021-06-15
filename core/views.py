from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from weather.service import WeatherService
from core import models


def index(request):
    # TODO: login page
    return HttpResponse("Hello, world. You're at the polls index.")


class DashboardView(View):

    def get(self, request):
        today_weather = WeatherService().get_weather()
        user_bias = models.UserBias.get_or_initialize_bias(request.user)
        recommended_clothes = models.Recommendation.get_recommendation(today_weather, user_bias)
        context = {'temperature': '10', 'head': 'gorro', 'body': 'campera', 'legs': 'jeans'}
        return render(request, 'core/dashboard.html', context)


class FeedbackView(View):
    # TODO: feedback form
    def post(self, request):
        return HttpResponse("you posted")
