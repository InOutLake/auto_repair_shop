from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('clients', clients, name='clients'),
    path('work', work, name='work'),
    path('cars', cars, name='cars'),
]
