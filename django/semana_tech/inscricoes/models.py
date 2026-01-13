from django.db import models

# Create your models here.
class Participantes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
