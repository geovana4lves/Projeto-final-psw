from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa(AbstractUser):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14) 
    data_nascimento = models.DateField()
    logradouro = models.CharField(max_length=100)
    numero =  models.IntegerField()
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50) 
    
    REQUIRED_FIELDS = [
        'email', 'nome', 'cpf', 'data_nascimento', 'logradouro',
        'numero', 'complemento', 'bairro', 'cidade', 'estado',
    ]   

    def __str__(self):
        return self.nome