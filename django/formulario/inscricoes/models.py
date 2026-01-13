from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome