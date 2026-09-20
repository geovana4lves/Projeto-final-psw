from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Disciplina
from .forms import DisciplinaForm


@login_required
@permission_required(
    'disciplina.view_disciplina',
    raise_exception=True
)
def listar_disciplinas(request):

    disciplinas = Disciplina.objects.all()

    return render(
        request,
        'disciplina/listar.html',
        {
            'disciplinas': disciplinas
        }
    )


@login_required
@permission_required(
    'disciplina.add_disciplina',
    raise_exception=True
)
def criar_disciplina(request):

    if request.method == 'POST':

        form = DisciplinaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Disciplina cadastrada com sucesso!'
            )

            return redirect('listar_disciplinas')

    else:

        form = DisciplinaForm()

    return render(
        request,
        'disciplina/criar.html',
        {
            'form': form
        }
    )


@login_required
@permission_required(
    'disciplina.change_disciplina',
    raise_exception=True
)
def editar_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    if request.method == 'POST':

        form = DisciplinaForm(
            request.POST,
            instance=disciplina
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Disciplina atualizada com sucesso!'
            )

            return redirect(
                'detalhes_disciplina',
                id=disciplina.id
            )

    else:

        form = DisciplinaForm(
            instance=disciplina
        )

    return render(
        request,
        'disciplina/editar.html',
        {
            'form': form,
            'disciplina': disciplina
        }
    )


@login_required
@permission_required(
    'disciplina.view_disciplina',
    raise_exception=True
)
def detalhar_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    return render(
        request,
        'disciplina/detalhes.html',
        {
            'disciplina': disciplina
        }
    )


@login_required
@permission_required(
    'disciplina.delete_disciplina',
    raise_exception=True
)
def deletar_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    if request.method == 'POST':

        nome = disciplina.nome

        disciplina.delete()

        messages.success(
            request,
            f'Disciplina "{nome}" excluída com sucesso!'
        )

        return redirect('listar_disciplinas')

    return render(
        request,
        'disciplina/deletar.html',
        {
            'disciplina': disciplina
        }
    )