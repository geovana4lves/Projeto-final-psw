from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
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
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def save(self, commit=True):
        pessoa = super().save(commit=False)

        pessoa.set_unusable_password()

        if commit:
            pessoa.save()

        return pessoa