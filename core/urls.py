from django.conf.urls import include, url
from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r"^accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('feedback/', login_required(views.FeedbackView.as_view()), name='feedback'),
]
