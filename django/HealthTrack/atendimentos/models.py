from django.db import models
from django.contrib.auth.models import User
from core.models import Paciente
# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self): return self.nome

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    crm = models.CharField(max_length=20)

    def __str__(self): return self.user.username

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    receita = models.TextField()

    def __str__(self): return f"Consulta {self.id} - {self.paciente}"