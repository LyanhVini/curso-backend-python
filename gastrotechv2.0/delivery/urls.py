# delivery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # A rota vazia '' é a página inicial do site
    path('', views.home_pedido_rapido, name='home'),
]