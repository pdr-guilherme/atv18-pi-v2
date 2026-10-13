from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from core.forms import ProjetoForm, TarefaForm
from core.models import Projeto, Tarefa


def projeto_list(request):
    projetos = Projeto.objects.all()
    return render(request, "core/projeto_list.html", {"projetos": projetos})


def projeto_create(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Projeto cadastrado com sucesso!")
            return redirect("core:projeto_list")
    else:
        form = ProjetoForm()

    return render(
        request,
        "core/projeto_form.html",
        {
            "form": form,
            "titulo": "Novo projeto",
            "botao": "Cadastrar",
        },
    )


def projeto_update(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, "Projeto atualizado com sucesso!")
            return redirect("core:projeto_list")
    else:
        form = ProjetoForm(instance=projeto)

    return render(
        request,
        "core/projeto_form.html",
        {
            "form": form,
            "titulo": "Editar projeto",
            "botao": "Salvar alterações",
        },
    )


def projeto_delete(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == "POST":
        projeto.delete()
        messages.success(request, "Projeto excluído com sucesso!")
        return redirect("core:projeto_list")

    return render(request, "core/projeto_confirm_delete.html", {"projeto": projeto})


def tarefa_list(request):
    tarefas = Tarefa.objects.select_related("projeto")
    return render(request, "core/tarefa_list.html", {"tarefas": tarefas})


def tarefa_create(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa criada com sucesso!")
            return redirect("core:tarefa_list")
    else:
        form = TarefaForm()

    return render(
        request,
        "core/tarefa_form.html",
        {
            "form": form,
            "titulo": "Nova tarefa",
            "botao": "Cadastrar",
        },
    )


def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada com sucesso!")
            return redirect("core:tarefa_list")
    else:
        form = TarefaForm(instance=tarefa)

    return render(
        request,
        "core/tarefa_form.html",
        {
            "form": form,
            "titulo": "Editar tarefa",
            "botao": "Salvar alterações",
        },
    )


def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        tarefa.delete()
        messages.success(request, "Tarefa excluída com sucesso!")
        return redirect("core:tarefa_list")

    return render(request, "core/tarefa_confirm_delete.html", {"tarefa": tarefa})
