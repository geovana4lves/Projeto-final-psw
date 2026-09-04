from django import forms
from .models import Matricula


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = [
            'pessoa',
            'turma',
            'data_matricula'
        ]

        widgets = {
            'data_matricula': forms.DateInput(
                attrs={'type': 'date'}
            )
        }