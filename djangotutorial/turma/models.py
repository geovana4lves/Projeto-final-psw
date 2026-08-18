from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='turmas'
    )

    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='turmas'
    )

    def __str__(self):
        return self.nome
