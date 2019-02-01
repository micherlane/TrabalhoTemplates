
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

