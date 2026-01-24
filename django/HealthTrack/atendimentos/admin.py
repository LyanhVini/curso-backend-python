from django.contrib import admin
from .models import Especialidade, Medico, Prontuario
from django.db import models

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('user', 'crm', 'especialidade')

admin.site.register(Especialidade)

class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'receita')

    actions = ['adicionar_observacao_padrao']
    @admin.action(description='Adicionar observação padrão')
    def adicionar_observacao_padrao(self, request, queryset):
        updated = queryset.update(descricao=models.F('descricao') + '\n\nRetorno sugerido em 30 dias.')
        self.message_user(request, f'{updated} prontuários atualizados com sucesso.')

# Register your models here.
