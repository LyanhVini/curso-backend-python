from django.contrib import admin
from .models import Participante, ProdutoLoja, Venda

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vip', 'codigo_ingresso') 
    list_filter = ('vip',)
    search_fields = ('nome', 'codigo_ingresso')
    readonly_fields = ('codigo_ingresso',)

admin.site.register(ProdutoLoja)
admin.site.register(Venda)