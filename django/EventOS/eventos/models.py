from django.db import models
import uuid

class Participante(models.Model):
    # UUID gera códigos únicos como 'a8098c1a-f86e-11da-bd1a-00112444be1e'
    codigo_ingresso = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=100)
    vip = models.BooleanField(default=False)
    
    def __str__(self): return self.nome

class ProdutoLoja(models.Model):
    codigo_barras = models.CharField(max_length=13, unique=True) # EAN-13
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self): return self.nome

class Venda(models.Model):
    produto = models.ForeignKey(ProdutoLoja, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.quantidade}x {self.produto.nome}"