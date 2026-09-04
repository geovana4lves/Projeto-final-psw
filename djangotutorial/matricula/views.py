from django.shortcuts import render, redirect
from .models import Matricula
from .forms import MatriculaForm


def listar_matriculas(request):
    matriculas = Matricula.objects.all()

    return render(
        request,
        'matricula/listar.html',
        {'matriculas': matriculas}
    )


def criar_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_matriculas')

    else:
        form = MatriculaForm()

    return render(
        request,
        'matricula/criar.html',
        {'form': form}
    )
