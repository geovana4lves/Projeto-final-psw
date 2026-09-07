from django.urls import path
from .views import criar_turma, listar_turmas, editar_turma, detalhar_turma, deletar_turma

urlpatterns = [
    path('criar/', criar_turma, name='criar_turma'),
    path('listar/', listar_turmas, name='listar_turmas'),
    path('editar/<int:id>/', editar_turma, name='editar_turma'),
    path('detalhes/<int:id>/', detalhar_turma, name='detalhes_turma'),
    path('deletar/<int:id>/', deletar_turma, name='deletar_turma'),
]