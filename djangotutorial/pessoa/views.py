from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm


def listar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'pessoa/listar.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')

    else:
        form = PessoaForm()
    return render(request, 'pessoa/criar.html', {'form': form})

def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect("listar_pessoas")
    else:
        form = PessoaForm(instance=pessoa)

    context = {"form": form, "pessoa": pessoa}
    return render(request, "pessoa/editar.html", context)
        
def detalhar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    context = {"pessoa": pessoa}
    return render(request, "pessoa/detalhes.html", context)

def deletar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == "POST":
        pessoa.delete()
        return redirect("listar_pessoas")

    return render(request, "pessoa/deletar.html", {"pessoa": pessoa})