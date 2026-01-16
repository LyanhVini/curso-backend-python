from django.contrib import admin
from .models import Documento
# Register your models here.

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'dono', 'status', 'ver_arquivo')
    search_fields = ('titulo', 'dono__username')
    
    @admin.display(description='Arquivo')
    def ver_arquivo(self, obj):
        return "Sim" if obj.arquivo else "Não"