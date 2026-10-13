from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjetoForm
from .models import Projeto


def projeto_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projeto_list.html', {'projetos': projetos})


def projeto_create(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('core:projeto_list')
    else:
        form = ProjetoForm()

    return render(request, 'core/projeto_form.html', {
        'form': form,
        'titulo': 'Novo projeto',
        'botao': 'Cadastrar',
    })


def projeto_update(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('core:projeto_list')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'core/projeto_form.html', {
        'form': form,
        'titulo': 'Editar projeto',
        'botao': 'Salvar alterações',
    })


def projeto_delete(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('core:projeto_list')

    return render(request, 'core/projeto_confirm_delete.html', {'projeto': projeto})