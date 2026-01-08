from django.contrib import admin
from django.contrib import messages
from .models import Prato, Pedido, ItemPedido
# Register your models here.

admin.site.site_header = "Administração Gastrotech"
admin.site.site_title = "Gastrotech"
admin.site.index_title = "Painel de Administração Gastrotech"

# --- MISSÃO 1: ENGENHARIA DE VISUALIZAÇÃO (Prato) ---
@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    # Ref: Slide 7 - Tabela Rica
    list_display = ('id', 'nome', 'categoria', 'preco', 'estoque', 'calcular_faturamento', 'ativo')
    
    # Ref: Slide 11 - Edição Rápida
    # Aviso: Campos em list_editable DEVEM estar em list_display
    list_editable = ('preco', 'estoque', 'ativo')
    
    # Ref: Slide 9 - Filtros Laterais
    list_filter = ('categoria', 'ativo')
    
    # Ref: Slide 10 - Busca (Google Interno)
    search_fields = ('nome',)
    
    # Configuração de Paginação (Ref: Slide 12)
    list_per_page = 10

    # Ref: Slide 8 - Campo Calculado (KPI Visual)
    @admin.display(description='💰 Prev. Faturamento')
    def calcular_faturamento(self, obj):
        faturamento = obj.preco * obj.estoque
        return f"R$ {faturamento:.2f}"


# --- CONFIGURAÇÃO DO INLINE (Auxiliar para Missão 2) ---
# Ref: Slide 14 - TabularInline
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1 # Mostra 1 linha vazia para adicionar itens
    autocomplete_fields = ['prato'] # Otimização se tiver muitos pratos (opcional)


# --- MISSÃO 2 e 3: MESTRE-DETALHE E AUTOMAÇÃO (Pedido) ---
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Visualização básica na lista
    list_display = ('id', 'cliente_nome', 'status', 'data_pedido', 'atendente')
    list_filter = ('status', 'data_pedido')
    
    # Ref: Slide 13 - Inlines (Adicionar itens na mesma tela)
    inlines = [ItemPedidoInline]
    
    # Ref: Slide 16 - Imutabilidade (Segurança de Dados)
    readonly_fields = ('data_pedido', 'atendente')

    # Ref: Slide 15 - Fieldsets (Organização Visual)
    fieldsets = (
        ('Dados do Cliente', {
            'fields': ('cliente_nome', 'cliente_endereco')
        }),
        ('Controle Interno', {
            'classes': ('collapse',), # Começa fechado para limpar a tela
            'fields': ('status', 'atendente', 'data_pedido')
        }),
    )

    # --- MISSÃO 3.1: ACTIONS (Workflow em Lote) ---
    # Ref: Slide 18 e 20
    @admin.action(description='✅ Marcar selecionados como ENTREGUE')
    def marcar_como_entregue(self, request, queryset):
        # update() é mais eficiente que salvar um por um
        atualizados = queryset.update(status='ENTREGUE')
        
        # Feedback visual para o usuário
        self.message_user(
            request, 
            f"{atualizados} pedidos foram atualizados para ENTREGUE com sucesso!", 
            messages.SUCCESS
        )
    
    # Registrando a action no admin
    actions = [marcar_como_entregue]

    # --- MISSÃO 3.2: AUDITORIA (Save Model) ---
    # Ref: Slide 22
    def save_model(self, request, obj, form, change):
        # Se o pedido não tem atendente (criação), define quem está logado
        if not obj.atendente:
            obj.atendente = request.user
        
        # Chama o save original para gravar no banco
        super().save_model(request, obj, form, change)
