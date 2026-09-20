from django.urls import path
from . import views


urlpatterns = [

    path(
        'criar/',
        views.criar_curso,
        name='criar_curso'
    ),

    path(
        'listar/',
        views.listar_cursos,
        name='listar_cursos'
    ),

    path(
        'editar/<int:id>/',
        views.editar_curso,
        name='editar_curso'
    ),

    path(
        'detalhes/<int:id>/',
        views.detalhes_curso,
        name='detalhes_curso'
    ),

    path(
        'deletar/<int:id>/',
        views.deletar_curso,
        name='deletar_curso'
    ),

]