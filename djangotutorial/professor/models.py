from django.db import models
from pessoa.models import Pessoa

class Professor(Pessoa):
    formacao = models.CharField(max_length=100)
    titulacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome