from django.contrib import admin
from django.contrib import messages
from .models import Prato, Pedido, ItemPedido
# Register your models here.

admin.site.site_header = "Administração Gastrotech"
admin.site.site_title = "Gastrotech"
admin.site.index_title = "Painel de Administração Gastrotech"

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'estoque', 
                    'preco', 'calcular_faturamento', 'ativo')
    list_editable = ('preco', 'estoque', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome',)
    
    @admin.display(description='Faturamento Estimado')
    def calcular_faturamento(self, obj):
        faturamento = obj.preco * obj.estoque
        return f'R$ {faturamento}'