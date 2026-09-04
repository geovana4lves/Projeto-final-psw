from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_matriculas, name='listar_matriculas'),
    path('criar/', views.criar_matricula, name='criar_matricula'),
]