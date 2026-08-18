from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='disciplinas'
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='disciplinas'
    )

    def __str__(self):
        return self.nome