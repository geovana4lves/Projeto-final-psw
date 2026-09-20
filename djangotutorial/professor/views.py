from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Professor
from .forms import ProfessorForm


@login_required
@permission_required(
    'professor.view_professor',
    raise_exception=True
)
def listar_professores(request):

    professores = Professor.objects.all()

    return render(
        request,
        'professor/listar.html',
        {
            'professores': professores
        }
    )


@login_required
@permission_required(
    'professor.add_professor',
    raise_exception=True
)
def criar_professor(request):

    if request.method == 'POST':

        form = ProfessorForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Professor cadastrado com sucesso!'
            )

            return redirect('listar_professores')

    else:

        form = ProfessorForm()

    return render(
        request,
        'professor/criar.html',
        {
            'form': form
        }
    )


@login_required
@permission_required(
    'professor.change_professor',
    raise_exception=True
)
def editar_professor(request, id):

    professor = get_object_or_404(
        Professor,
        id=id
    )

    if request.method == 'POST':

        form = ProfessorForm(
            request.POST,
            instance=professor
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Professor atualizado com sucesso!'
            )

            return redirect(
                'detalhes_professor',
                id=professor.id
            )

    else:

        form = ProfessorForm(
            instance=professor
        )

    return render(
        request,
        'professor/editar.html',
        {
            'form': form,
            'professor': professor
        }
    )


@login_required
@permission_required(
    'professor.view_professor',
    raise_exception=True
)
def detalhar_professor(request, id):

    professor = get_object_or_404(
        Professor,
        id=id
    )

    return render(
        request,
        'professor/detalhes.html',
        {
            'professor': professor
        }
    )


@login_required
@permission_required(
    'professor.delete_professor',
    raise_exception=True
)
def deletar_professor(request, id):

    professor = get_object_or_404(
        Professor,
        id=id
    )

    if request.method == 'POST':

        nome = professor.nome

        professor.delete()

        messages.success(
            request,
            f'Professor "{nome}" excluído com sucesso!'
        )

        return redirect('listar_professores')

    return render(
        request,
        'professor/deletar.html',
        {
            'professor': professor
        }
    )