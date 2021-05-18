from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Covid_Forecast', views.Covid_Forecast, name='Covid_Forecast'),
    path('India_Trend', views.India_Trend, name='India_Trend'),
    path('Global_Trend', views.Global_Trend, name='Global_Trend'),
    path('About_Covid', views.About_Covid, name='About_Covid'),
    path('Contact', views.Contact, name='Contact'),
    path('Test_Yourself', views.Test_Yourself, name='Test_Yourself'),
    path('bot_search', views.bot_search, name='bot_search'),
]
