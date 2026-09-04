from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm


def listar_cursos(request):
    cursos = Curso.objects.all()

    return render(
        request,
        'curso/listar.html',
        {'cursos': cursos}
    )


def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

    else:
        form = CursoForm()

    return render(
        request,
        'curso/criar.html',
        {'form': form}
    )
