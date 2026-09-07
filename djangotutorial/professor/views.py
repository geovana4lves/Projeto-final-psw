from django.shortcuts import render, redirect, get_object_or_404
from .models import Professor
from .forms import ProfessorForm


def listar_professores(request):
    professores = Professor.objects.all()

    return render(request, 'professor/listar.html', {'professores': professores})

def criar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_professores')

    else:
        form = ProfessorForm()

    return render(request, 'professor/criar.html', {'form': form})

def editar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)

    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect("listar_professores")
    else:
        form = ProfessorForm(instance=professor)

    context = {"form": form, "professor": professor}
    return render(request, "professor/editar.html", context)

def detalhar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)

    context = {"professor": professor}
    return render(request, "professor/detalhes.html", context)

def deletar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)

    if request.method == "POST":
        professor.delete()
        return redirect("listar_professores")

    return render(request, "professor/deletar.html", {"professor": professor})