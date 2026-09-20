from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q

from .models import Matricula
from .forms import MatriculaForm


@login_required
@permission_required('matricula.view_matricula', raise_exception=True)
def listar_matriculas(request):

    q = request.GET.get('q', '').strip()

    matriculas = Matricula.objects.select_related(
        'pessoa',
        'turma',
        'turma__curso'
    )

    if q:
        matriculas = matriculas.filter(
            Q(pessoa__nome__icontains=q) |
            Q(pessoa__username__icontains=q) |
            Q(turma__nome__icontains=q) |
            Q(turma__curso__nome__icontains=q)
        )

    matriculas = matriculas.order_by(
        '-data_matricula'
    )

    return render(
        request,
        'matricula/listar.html',
        {
            'matriculas': matriculas,
            'q': q
        }
    )


@login_required
@permission_required('matricula.add_matricula', raise_exception=True)
def criar_matricula(request):

    if request.method == 'POST':

        form = MatriculaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Matrícula realizada com sucesso!'
            )

            return redirect('listar_matriculas')

    else:

        form = MatriculaForm()

    return render(
        request,
        'matricula/criar.html',
        {'form': form}
    )


@login_required
@permission_required('matricula.change_matricula', raise_exception=True)
def editar_matricula(request, id):

    matricula = get_object_or_404(
        Matricula,
        id=id
    )

    if request.method == 'POST':

        form = MatriculaForm(
            request.POST,
            instance=matricula
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Matrícula atualizada com sucesso!'
            )

            return redirect(
                'detalhes_matricula',
                id=matricula.id
            )

    else:

        form = MatriculaForm(
            instance=matricula
        )

    return render(
        request,
        'matricula/editar.html',
        {
            'form': form,
            'matricula': matricula
        }
    )


@login_required
@permission_required('matricula.view_matricula', raise_exception=True)
def detalhar_matricula(request, id):

    matricula = get_object_or_404(
        Matricula.objects.select_related(
            'pessoa',
            'turma',
            'turma__curso'
        ),
        id=id
    )

    return render(
        request,
        'matricula/detalhes.html',
        {'matricula': matricula}
    )


@login_required
@permission_required('matricula.delete_matricula', raise_exception=True)
def deletar_matricula(request, id):

    matricula = get_object_or_404(
        Matricula,
        id=id
    )

    if request.method == 'POST':

        nome = matricula.pessoa.nome

        matricula.delete()

        messages.success(
            request,
            f'Matrícula de "{nome}" excluída com sucesso!'
        )

        return redirect('listar_matriculas')

    return render(
        request,
        'matricula/deletar.html',
        {'matricula': matricula}
    )