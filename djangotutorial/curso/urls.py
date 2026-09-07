from django.urls import path
from .views import criar_curso, listar_cursos, editar_curso, detalhar_curso, deletar_curso

urlpatterns = [
    path('criar/', criar_curso, name='criar_curso'),
    path('listar/', listar_cursos, name='listar_cursos'),
    path('editar/<int:id>/', editar_curso, name='editar_curso'),
    path('detalhes/<int:id>/', detalhar_curso, name='detalhes_curso'),
    path('deletar/<int:id>/', deletar_curso, name='deletar_curso'),
]