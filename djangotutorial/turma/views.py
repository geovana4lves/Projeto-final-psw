from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Turma
from .forms import TurmaForm

@login_required
@permission_required('turma.view_turma', raise_exception=True)
def listar_turmas(request):
    turmas = Turma.objects.all()

    return render(request, 'turma/listar.html', {'turmas': turmas})

@login_required
@permission_required('turma.add_turma', raise_exception=True)
def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_turmas')

    else:
        form = TurmaForm()

    return render(request, 'turma/criar.html', {'form': form})

@login_required
@permission_required('turma.change_turma', raise_exception=True)
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

@login_required
@permission_required('turma.view_turma', raise_exception=True)
def detalhar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)

    context = {"turma": turma}
    return render(request, "turma/detalhes.html", context)

@login_required
@permission_required('turma.delete_turma', raise_exception=True)
def deletar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)

    if request.method == "POST":
        turma.delete()
        return redirect("listar_turmas")

    return render(request, "turma/deletar.html", {"turma": turma})