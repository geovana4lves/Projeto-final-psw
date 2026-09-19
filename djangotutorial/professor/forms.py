from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Professor


class ProfessorForm(UserCreationForm):
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
            'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        }
