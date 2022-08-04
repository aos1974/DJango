"""lesson1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter

from demo.converters import DateConverters
from demo.views import index, get_time, hello, sum, echo_date, pagi, create_car, list_car
from demo.views import create_person, list_person

register_converter(DateConverters, 'date')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('time/', get_time),
    path('hello/', hello),
    path('sum/<a>/<b>/', sum),
    path('echo-date/<date:dt>/', echo_date),
    path('pagi/', pagi),
    path('new_car/', create_car),
    path('cars/', list_car),
    path('new_person/', create_person),
    path('persons/', list_person),
]
