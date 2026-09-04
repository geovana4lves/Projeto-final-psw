from django.shortcuts import render, redirect
from .models import Turma
from .forms import TurmaForm


def listar_turmas(request):
    turmas = Turma.objects.all()

    return render(
        request,
        'turma/listar.html',
        {'turmas': turmas}
    )


def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_turmas')

    else:
        form = TurmaForm()

    return render(
        request,
        'turma/criar.html',
        {'form': form}
    )
