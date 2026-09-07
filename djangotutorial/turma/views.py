from django.shortcuts import render, redirect, get_object_or_404
from .models import Turma
from .forms import TurmaForm


def listar_turmas(request):
    turmas = Turma.objects.all()

    return render(request, 'turma/listar.html', {'turmas': turmas})

def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_turmas')

    else:
        form = TurmaForm()

    return render(request, 'turma/criar.html', {'form': form})

def editar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)

    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect("listar_turmas")
    else:
        form = TurmaForm(instance=turma)

    context = {"form": form, "turma": turma}
    return render(request, "turma/editar.html", context)

def detalhar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)

    context = {"turma": turma}
    return render(request, "turma/detalhes.html", context)

def deletar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)

    if request.method == "POST":
        turma.delete()
        return redirect("listar_turmas")

    return render(request, "turma/deletar.html", {"turma": turma})