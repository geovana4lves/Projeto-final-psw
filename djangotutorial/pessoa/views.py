from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q

from .models import Pessoa
from .forms import PessoaForm


@login_required
@permission_required('pessoa.view_pessoa', raise_exception=True)
def listar_pessoas(request):

    q = request.GET.get('q', '').strip()

    pessoas = Pessoa.objects.all()

    if q:
        pessoas = pessoas.filter(
            Q(nome__icontains=q) |
            Q(username__icontains=q) |
            Q(email__icontains=q) |
            Q(cpf__icontains=q) |
            Q(cidade__icontains=q)
        )

    pessoas = pessoas.order_by('nome')

    return render(
        request,
        'pessoa/listar.html',
        {
            'pessoas': pessoas,
            'q': q
        }
    )


def criar_pessoa(request):

    if request.method == 'POST':

        form = PessoaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Conta criada com sucesso! Agora faça login para acessar o sistema.'
            )

            return redirect('login')

    else:

        form = PessoaForm()

    return render(
        request,
        'pessoa/criar.html',
        {'form': form}
    )


@login_required
@permission_required('pessoa.change_pessoa', raise_exception=True)
def editar_pessoa(request, id):

    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'POST':

        form = PessoaForm(
            request.POST,
            instance=pessoa
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Pessoa atualizada com sucesso!'
            )

            return redirect(
                'detalhes_pessoa',
                id=pessoa.id
            )

    else:

        form = PessoaForm(instance=pessoa)

    return render(
        request,
        'pessoa/editar.html',
        {
            'form': form,
            'pessoa': pessoa
        }
    )


@login_required
@permission_required('pessoa.view_pessoa', raise_exception=True)
def detalhar_pessoa(request, id):

    pessoa = get_object_or_404(Pessoa, id=id)

    return render(
        request,
        'pessoa/detalhes.html',
        {'pessoa': pessoa}
    )


@login_required
@permission_required('pessoa.delete_pessoa', raise_exception=True)
def deletar_pessoa(request, id):

    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'POST':

        nome = pessoa.nome

        pessoa.delete()

        messages.success(
            request,
            f'Pessoa "{nome}" excluída com sucesso!'
        )

        return redirect('listar_pessoas')

    return render(
        request,
        'pessoa/deletar.html',
        {'pessoa': pessoa}
    )