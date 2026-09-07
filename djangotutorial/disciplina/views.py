from django.shortcuts import render, redirect, get_object_or_404
from .models import Disciplina
from .forms import DisciplinaForm


def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()

    return render(request, 'disciplina/listar.html', {'disciplinas': disciplinas})


def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'disciplina/criar.html', {'form': form})
    
def editar_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect("listar_disciplinas")
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {"form": form, "disciplina": disciplina}
    return render(request, "disciplina/editar.html", context) 

def detalhar_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    context = {"disciplina": disciplina}
    return render(request, "disciplina/detalhes.html", context)

def deletar_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == "POST":
        disciplina.delete()
        return redirect("listar_disciplinas")

    return render(request, "disciplina/deletar.html", {"disciplina": disciplina})  