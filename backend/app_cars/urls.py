from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings

app_name = 'app_cars'
urlpatterns = [
    path('car_list/', views.car_list, name='car_list'),
]





