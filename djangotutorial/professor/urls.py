from django.urls import path
from .views import criar_professor, listar_professores, editar_professor, detalhar_professor, deletar_professor

urlpatterns = [
    path('criar/', criar_professor, name='criar_professor'),
    path('listar/', listar_professores, name='listar_professores'),
    path('editar/<int:id>/', editar_professor, name='editar_professor'),
    path('detalhes/<int:id>/', detalhar_professor, name='detalhes_professor'),
    path('deletar/<int:id>/', deletar_professor, name='deletar_professor'),
]