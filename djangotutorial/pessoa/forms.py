from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa


class PessoaForm(UserCreationForm):
    class Meta:
        model = Pessoa
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
            'estado'
        ]

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        }