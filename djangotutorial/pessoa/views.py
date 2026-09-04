from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm


def listar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(
        request,
        'pessoa/listar.html',
        {'pessoas': pessoas}
    )


def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')

    else:
        form = PessoaForm()

    return render(
        request,
        'pessoa/criar.html',
        {'form': form}
    )
