from django.urls import path
from .views import criar_pessoa, listar_pessoas, editar_pessoa, detalhar_pessoa, deletar_pessoa

urlpatterns = [
    path('criar/', criar_pessoa, name='criar_pessoa'),
    path('listar/', listar_pessoas, name='listar_pessoas'),
    path('editar/<int:id>/', editar_pessoa, name='editar_pessoa'),
    path('detalhes/<int:id>/', detalhar_pessoa, name='detalhes_pessoa'),
    path('deletar/<int:id>/', deletar_pessoa, name='deletar_pessoa'),
]