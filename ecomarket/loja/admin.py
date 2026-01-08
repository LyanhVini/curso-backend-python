from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    "Registrar dados no DB"
    #view_on_site = True
    list_display = ('nome', 'preco', 'produtor')
    list_filter = ('preco', 'produtor')
    search_fields = ('nome', 'produtor')
    list_editable = ('preco', 'produtor')


#admin.site.register(Produto, ProdutoAdmin)
admin.site.site_header = "🏢 ECOMARKET BFD"
admin.site.site_title = "Painel Administrativo"
admin.site.index_title = "📊 Dashboard de Produtos"


