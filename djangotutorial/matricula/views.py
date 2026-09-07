from django.shortcuts import render, redirect, get_object_or_404
from .models import Matricula
from .forms import MatriculaForm


def listar_matriculas(request):
    matriculas = Matricula.objects.all()

    return render(request, 'matricula/listar.html', {'matriculas': matriculas})


def criar_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_matriculas')
    else:
        form = MatriculaForm()
    return render(request, 'matricula/criar.html', {'form': form})

def editar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)

    if request.method == "POST":
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect("listar_matriculas")
    else:
        form = MatriculaForm(instance=matricula)

    context = {"form": form, "matricula": matricula}
    return render(request, "matricula/editar.html", context)

def detalhar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)

    context = {"matricula": matricula}
    return render(request, "matricula/detalhes.html", context)

def deletar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)

    if request.method == "POST":
        matricula.delete()
        return redirect("listar_matriculas")

    return render(request, "matricula/deletar.html", {"matricula": matricula})