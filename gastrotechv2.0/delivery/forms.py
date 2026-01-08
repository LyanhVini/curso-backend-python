from django import forms
from .models import Pedido, Prato

class PedidoRapidoForm(forms.ModelForm):
    # --- CAMPO EXTRA (Não está diretamente no modelo Pedido) ---
    # Criamos um campo dropdown (select) que lista todos os Pratos ativos do banco.
    prato_escolhido = forms.ModelChoiceField(
        queryset=Prato.objects.filter(ativo=True),
        empty_label="Selecione um prato delicioso...",
        widget=forms.Select(attrs={'class': 'form-select form-select-lg'}),
        label="Qual será o pedido de hoje?"
    )

    class Meta:
        model = Pedido
        # Campos que vêm direto do modelo Pedido
        fields = ['cliente_nome', 'cliente_endereco']
        
        # Personalizando os inputs com Bootstrap
        widgets = {
            'cliente_nome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Seu nome completo'
            }),
            'cliente_endereco': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Rua, número, bairro e ponto de referência...'
            }),
        }
        labels = {
            'cliente_nome': 'Quem vai receber?',
            'cliente_endereco': 'Onde entregamos?',
        }