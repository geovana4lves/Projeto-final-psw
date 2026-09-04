from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_disciplinas, name='listar_disciplinas'),
    path('criar/', views.criar_disciplina, name='criar_disciplina'),
]