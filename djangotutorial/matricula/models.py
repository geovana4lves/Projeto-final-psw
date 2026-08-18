from django.db import models

class Matricula(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )

    data_matricula = models.DateField()

    def __str__(self):
        return f'{self.pessoa.nome} - {self.turma.nome}'