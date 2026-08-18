from django.db import models
from django.contrib.auth.models import User

class Pessoa(User):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14) 
    data_nascimento = models.DateField()
    logradouro = models.CharField(max_length=100)
    numero =  models.IntegerField()
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)    

    def __str__(self):
        return self.nome