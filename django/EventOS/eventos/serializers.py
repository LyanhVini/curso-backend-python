from rest_framework import serializers
from .models import Participante, ProdutoLoja, Venda

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['nome', 'vip', 'codigo_ingresso']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoLoja
        fields = ['nome', 'preco', 'codigo_barras']

class VendaSerializer(serializers.ModelSerializer):
    
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    produto_preco = serializers.DecimalField(source='produto.preco', max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Venda
        fields = ['id', 'data', 'quantidade', 'produto_nome', 'produto_preco']