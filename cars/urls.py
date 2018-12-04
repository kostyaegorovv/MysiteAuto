from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'cars', views.cars, name='cars'),
]