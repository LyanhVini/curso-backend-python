from django.contrib import admin
from django.contrib import messages
from .models import Prato, Pedido, ItemPedido
from django import forms
# Register your models here.

admin.site.site_header = "Administração Gastrotech"
admin.site.site_title = "Gastrotech"
admin.site.index_title = "Painel de Administração Gastrotech"

class PratoAdminForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = '__all__'
        
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco
            
    def clean_estoque(self):
        estoque = self.cleaned_data.get('estoque')
        if estoque is not None and estoque < 0:
            raise forms.ValidationError("O estoque não pode ser negativo")
        return estoque
    
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            main_type, sub_type = foto.content_type.split('/')
            if main_type != 'image':
                raise forms.ValidationError("Envie apenas arquivos de imagem válidos (.jgp e .png)")
            
            if foto.size > 2 * 1024 * 1024:
                raise forms.ValidationError("A imagem é muito grande. Máximo de 2MB")
            
            return foto

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
    
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    autocomplete_fields = ['prato']

@admin.register(Pedido)  
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nome', 'status', 
                    'data_pedido', 'atendente')
    list_filter = ('status', 'data_pedido')
    inlines = [ItemPedidoInline]
    readonly_fields = ('data_pedido', 'atendente')
    fieldsets = (
        ('Dados do Cliente', {
            'fields': ('cliente_nome', 'cliente_endereco')
        }),
        ('Controle Interno', {
            'classes': ('collapse',),
            'fields': ('status', 'data_pedido', 'atendente')
        }),
    )
    
    @admin.action(description='Marcar pedidos como Entregues')
    def marcar_como_entregue(self, request, queryset):
        atualizados = queryset.update(status='ENTREGUE')
        self.message_user(
            request,
            f'{atualizados} pedidos marcados como Entregues.',
            messages.SUCCESS
        )

    actions = ['marcar_como_entregue']