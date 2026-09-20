from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q

from .models import Curso
from .forms import CursoForm


@login_required
@permission_required('curso.view_curso', raise_exception=True)
def listar_cursos(request):

    q = request.GET.get('q', '').strip()

    cursos = Curso.objects.all()

    if q:
        cursos = cursos.filter(
            Q(nome__icontains=q) |
            Q(tipo__icontains=q)
        )

    cursos = cursos.order_by('nome')

    return render(
        request,
        'curso/listar.html',
        {
            'cursos': cursos,
            'q': q
        }
    )


@login_required
@permission_required('curso.add_curso', raise_exception=True)
def criar_curso(request):

    if request.method == 'POST':

        form = CursoForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Curso cadastrado com sucesso!'
            )

            return redirect('listar_cursos')

    else:

        form = CursoForm()

    return render(
        request,
        'curso/criar.html',
        {'form': form}
    )


@login_required
@permission_required('curso.change_curso', raise_exception=True)
def editar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':

        form = CursoForm(
            request.POST,
            instance=curso
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Curso atualizado com sucesso!'
            )

            return redirect(
                'detalhes_curso',
                id=curso.id
            )

    else:

        form = CursoForm(instance=curso)

    return render(
        request,
        'curso/editar.html',
        {
            'form': form,
            'curso': curso
        }
    )


@login_required
@permission_required('curso.view_curso', raise_exception=True)
def detalhes_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    return render(
        request,
        'curso/detalhes.html',
        {'curso': curso}
    )


@login_required
@permission_required('curso.delete_curso', raise_exception=True)
def deletar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':

        nome = curso.nome

        curso.delete()

        messages.success(
            request,
            f'Curso "{nome}" excluído com sucesso!'
        )

        return redirect('listar_cursos')

    return render(
        request,
        'curso/deletar.html',
        {'curso': curso}
    )