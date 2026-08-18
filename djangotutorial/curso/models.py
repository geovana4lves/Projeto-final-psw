from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    carga_horaria_total = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome