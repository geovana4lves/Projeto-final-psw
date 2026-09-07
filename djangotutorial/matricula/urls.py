from django.urls import path
from .views import criar_matricula, listar_matriculas, editar_matricula, detalhar_matricula, deletar_matricula

urlpatterns = [
    path('criar/', criar_matricula, name='criar_matricula'),
    path('listar/', listar_matriculas, name='listar_matriculas'),
    path('editar/<int:id>/', editar_matricula, name='editar_matricula'),
    path('detalhes/<int:id>/', detalhar_matricula, name='detalhes_matricula'),
    path('deletar/<int:id>/', deletar_matricula, name='deletar_matricula'),
]