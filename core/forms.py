from django import forms

from core.models import Projeto, Tarefa


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ("nome", "descricao", "data_inicio")
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Nome do projeto"}),
            "descricao": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Descreva o projeto"}
            ),
            "data_inicio": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ("titulo", "prioridade", "concluido", "projeto")
