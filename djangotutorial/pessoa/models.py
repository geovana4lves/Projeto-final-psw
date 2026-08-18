from django.db import models
from django.contrib.auth.models import User

class Pessoa(User):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Professor(Pessoa):
    formacao = models.CharField(max_length=100)
    titulacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    carga_horaria_total = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


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