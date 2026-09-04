from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nome',
            'duracao',
            'carga_horaria_total',
            'tipo'
        ]