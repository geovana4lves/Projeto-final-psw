from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_professores, name='listar_professores'),
    path('criar/', views.criar_professor, name='criar_professor'),
]
