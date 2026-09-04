from django import forms
from .models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = [
            'username',
            'email',
            'nome',
            'cpf',
            'data_nascimento',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado',
            'formacao',
            'titulacao'
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def save(self, commit=True):
        professor = super().save(commit=False)

        professor.set_unusable_password()

        if commit:
            professor.save()

        return professor
    