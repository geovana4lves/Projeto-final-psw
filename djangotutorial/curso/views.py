from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar.html', {'cursos': cursos})

def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()

    return render(request, 'curso/criar.html', {'form': form})
    
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("listar_cursos")
    else:
        form = CursoForm(instance=curso)
        
    context = {"form": form, "curso": curso}
    return render(request, "curso/editar.html", context)

def detalhar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    context = {"curso": curso}
    return render(request, "curso/detalhes.html", context)

def deletar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == "POST":
        curso.delete()
        return redirect("listar_cursos")

    return render(request, "curso/deletar.html", {"curso": curso})