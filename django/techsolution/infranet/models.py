from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Funcionario(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    eh_gestor = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.cargo}"
    
    