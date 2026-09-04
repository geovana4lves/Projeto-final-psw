from django.shortcuts import render, redirect
from .models import Professor
from .forms import ProfessorForm


def listar_professores(request):
    professores = Professor.objects.all()

    return render(
        request,
        'professor/listar.html',
        {'professores': professores}
    )


def criar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_professores')

    else:
        form = ProfessorForm()

    return render(
        request,
        'professor/criar.html',
        {'form': form}
    )
