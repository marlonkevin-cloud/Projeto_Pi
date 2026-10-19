from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/form_projeto.html', {'form': form})

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('core:lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projetos/form_projeto.html', {'form': form, 'projeto': projeto})

def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('core:lista_projetos')
    return render(request, 'projetos/confirmar_exclusao.html', {'projeto': projeto})

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().select_related('projeto')
    return render(request, 'tarefas/listar.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/form.html', {'form': form, 'titulo_pagina': 'Criar Tarefa'})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core:listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/form.html', {'form': form, 'titulo_pagina': 'Editar Tarefa'})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('core:listar_tarefas')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})