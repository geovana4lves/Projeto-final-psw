from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_turmas, name='listar_turmas'),
    path('criar/', views.criar_turma, name='criar_turma'),
]
