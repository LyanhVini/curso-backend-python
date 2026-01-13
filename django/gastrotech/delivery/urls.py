from django.urls import path
from . import views

urlpatters = [
    path('', views.home_pedido_rapido, nome='home'),
]