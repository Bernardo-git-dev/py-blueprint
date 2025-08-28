# greeting/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GreetingView.as_view(), name='greeting'),
    path('<str:name>/', views.PersonalizedGreetingView.as_view(), name='personalized_greeting'),
]