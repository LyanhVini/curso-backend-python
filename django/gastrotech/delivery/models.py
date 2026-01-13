from django.db import models
from django.contrib.auth.models import User
# Create your models here.
  

class Prato(models.Model):

    CATEGORIAS = [
        ('ENTRADA', 'Entrada'),
        ('PRINCIPAL', 'Prato Principal'),
        ('BEBIDA', 'Bebida')
    ]
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Cardápio'

class Pedido(models.Model):
    
    STATUS = [
        ('PENDENTE', 'Pendente'),
        ('PREPARANDO', 'Preparando'),
        ('ENTREGUE', 'Entregue')
    ]
    
    cliente_nome = models.CharField(max_length=100)
    cliente_endereco = models.TextField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS)
    atendente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'Pedido #{self.id}'
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantidade} x {self.prato.nome}'