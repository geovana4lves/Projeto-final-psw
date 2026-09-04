from django.shortcuts import render, redirect
from .models import Disciplina
from .forms import DisciplinaForm


def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()

    return render(
        request,
        'disciplina/listar.html',
        {'disciplinas': disciplinas}
    )


def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')

    else:
        form = DisciplinaForm()

    return render(
        request,
        'disciplina/criar.html',
        {'form': form}
    )