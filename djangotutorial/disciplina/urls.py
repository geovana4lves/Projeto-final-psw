from django.urls import path
from .views import criar_disciplina, listar_disciplinas, editar_disciplina, detalhar_disciplina, deletar_disciplina

urlpatterns = [
    path('criar/', criar_disciplina, name='criar_disciplina'),
    path('listar/', listar_disciplinas, name='listar_disciplinas'),
    path('editar/<int:id>/', editar_disciplina, name='editar_disciplina'),
    path('detalhes/<int:id>/', detalhar_disciplina, name='detalhes_disciplina'),
    path('deletar/<int:id>/', deletar_disciplina, name='deletar_disciplina'),
]