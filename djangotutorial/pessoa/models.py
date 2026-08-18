from django.db import models
from django.contrib.auth.models import User

class Pessoa(User):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14) 
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome