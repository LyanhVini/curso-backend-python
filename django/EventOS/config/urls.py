from django.contrib import admin
from django.urls import path
from eventos import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- APIS JSON (EventOS) ---
    path('api/ingresso/<str:codigo>/', views.validar_ingresso),
    path('api/loja/preco/<str:ean>/', views.consultar_preco),
    path('api/dashboard/', views.dashboard_dados),
    path('api/vendas/recentes/', views.listar_vendas_otimizadas),

    # --- PDF ---
    path('imprimir/cracha/<str:codigo>/', views.gerar_cracha),



    # --- DOCUMENTAÇÃO SWAGGER (Bônus) ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]