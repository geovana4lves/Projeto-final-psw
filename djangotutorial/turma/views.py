from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q

from .models import Turma
from .forms import TurmaForm


@login_required
@permission_required('turma.view_turma', raise_exception=True)
def listar_turmas(request):

    q = request.GET.get('q', '').strip()

    turmas = Turma.objects.select_related('curso').all()

    if q:
        turmas = turmas.filter(
            Q(nome__icontains=q) |
            Q(curso__nome__icontains=q)
        )

    turmas = turmas.order_by('nome')

    return render(
        request,
        'turma/listar.html',
        {
            'turmas': turmas,
            'q': q
        }
    )


@login_required
@permission_required('turma.add_turma', raise_exception=True)
def criar_turma(request):

    if request.method == 'POST':

        form = TurmaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Turma cadastrada com sucesso!'
            )

            return redirect('listar_turmas')

    else:

        form = TurmaForm()

    return render(
        request,
        'turma/criar.html',
        {'form': form}
    )


@login_required
@permission_required('turma.change_turma', raise_exception=True)
def editar_turma(request, id):

    turma = get_object_or_404(Turma, id=id)

    if request.method == 'POST':

        form = TurmaForm(
            request.POST,
            instance=turma
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Turma atualizada com sucesso!'
            )

            return redirect(
                'detalhes_turma',
                id=turma.id
            )

    else:

        form = TurmaForm(instance=turma)

    return render(
        request,
        'turma/editar.html',
        {
            'form': form,
            'turma': turma
        }
    )


@login_required
@permission_required('turma.view_turma', raise_exception=True)
def detalhar_turma(request, id):

    turma = get_object_or_404(
        Turma.objects.select_related('curso'),
        id=id
    )

    return render(
        request,
        'turma/detalhes.html',
        {'turma': turma}
    )


@login_required
@permission_required('turma.delete_turma', raise_exception=True)
def deletar_turma(request, id):

    turma = get_object_or_404(Turma, id=id)

    if request.method == 'POST':

        nome = turma.nome

        turma.delete()

        messages.success(
            request,
            f'Turma "{nome}" excluída com sucesso!'
        )

        return redirect('listar_turmas')

    return render(
        request,
        'turma/deletar.html',
        {'turma': turma}
    )