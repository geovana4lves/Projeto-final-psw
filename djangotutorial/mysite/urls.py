from django.contrib import admin
from django.urls import path, include
from .views import home, painel


urlpatterns = [
    path('', home, name='home'),

    path('painel/', painel, name='painel'),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cursos/', include('curso.urls')),
    path('pessoas/', include('pessoa.urls')),
    path('professores/', include('professor.urls')),
    path('turmas/', include('turma.urls')),
    path('disciplinas/', include('disciplina.urls')),
    path('matriculas/', include('matricula.urls')),
]