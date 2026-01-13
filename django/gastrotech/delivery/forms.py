from django import forms
from .models import Prato, Pedido

class PedidoRapidoForm(forms.ModelForm):
    
    prato_escolhido = forms.ModelChoiceField(
        queryset=Prato.objects.filter(ative=True),
        empty_label="Selecione um prato",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Qual será o pedido de hoje?"
    )
    
    class Meta:
        model = Pedido
        fields = ['cliente_nome', 'cliente_endereco']
        
        widgets = {
            'cliente_nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'cliente_endereco': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
        labels = {
            'cliente_nome': 'Nome do Cliente',
            'cliente_endereco': 'Endereço de Entrega',
        }
        
        # VALIDAÇÂO SEMÂNTICA:
        def clean_cliente_endereco(self):
            endereco = self.cleaned_data.get('cliente_endereco')
            # o endereço deve ter pelo menos 10 caracteres
            if len(endereco) < 10:
                raise forms.ValidationError("Endereço muito curto.")
            return endereco
        
        # VALIDAÇÂO CRUZADA (regra de negócio):
        def clean(self):
            cleaned_data = super().clean()
            prato = cleaned_data.get('prato_escolhido')
            if prato:
                # Verificação do estoque
                if prato.estoque <= 0:
                    raise forms.ValidationError("Prato sem estoque.")
            return cleaned_data