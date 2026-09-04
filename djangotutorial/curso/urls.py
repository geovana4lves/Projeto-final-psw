from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('criar/', views.criar_curso, name='criar_curso'),
]
