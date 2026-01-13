from django.contrib import admin
from .models import Funcionario

# 1. Personalização do Cabeçalho (Branding)
admin.site.site_header = "Gestão TechSolutions"
admin.site.site_title = "Intranet Admin"
admin.site.index_title = "Painel de Controle de RH"

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # COLUNAS: O que aparece na lista
    list_display = ('user', 'cargo', 'departamento', 'eh_gestor')
    # EDIÇÃO RÁPIDA: Permite marcar/desmarcar gestor direto na lista!
    list_editable = ('eh_gestor',)
    # FILTROS LATERAIS: Para achar rápido quem é gestor ou de qual setor
    list_filter = ('eh_gestor', 'departamento')

    # BARRA DE PESQUISA: 
    # 'user__username' significa: "Vá na tabela User e busque pelo username"
    # 'user__first_name': Busca pelo primeiro nome também
    search_fields = ('cargo', 'user__username', 'user__first_name')

    # PAGINAÇÃO: Evita listas infinitas
    list_per_page = 10

    # ORGANIZAÇÃO DO FORMULÁRIO (Layout)
    fieldsets = (
        ('Vínculo de Sistema', {
            'fields': ('user',)
        }),
        ('Dados Profissionais', {
            'fields': ('cargo', 'departamento', 'eh_gestor'),
            'description': 'Informações utilizadas para controle de acesso na Intranet.'
        }),
    )
