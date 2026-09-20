from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from curso.models import Curso
from pessoa.models import Pessoa
from professor.models import Professor
from turma.models import Turma
from disciplina.models import Disciplina
from matricula.models import Matricula


def home(request):
    return render(
        request,
        'home.html'
    )


@login_required
def painel(request):

    contexto = {
        'total_cursos': Curso.objects.count(),
        'total_pessoas': Pessoa.objects.count(),
        'total_professores': Professor.objects.count(),
        'total_turmas': Turma.objects.count(),
        'total_disciplinas': Disciplina.objects.count(),
        'total_matriculas': Matricula.objects.count(),
    }

    return render(
        request,
        'painel.html',
        contexto
    )


def erro_403(request, exception=None):

    return render(
        request,
        '403.html',
        status=403
    )