from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Documento(models.Model):
    status_c = [
        ('PEN', 'Pendente'),
        ('APR', 'Aprovado'),
        ('REJ', 'Rejeitado'),
    ]
    
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='docs/')
    status = models.CharField(max_length=3,
                              choices=status_c,
                              default='PEN')
    dono = models.ForeignKey(User, 
                             on_delete=models.CASCADE)
    
    def __str__(self): return self.titulo
