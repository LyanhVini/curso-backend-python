from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:filme_id>/', views.adicionar_ao_pedido, name='add'),
    path('sacola/', views.ver_sacola, name='ver_sacola'),
    path('limpar/', views.limpar_sacola, name='limpar'),
    path('checkout/', views.finalizar_pedido, name='checkout')
]