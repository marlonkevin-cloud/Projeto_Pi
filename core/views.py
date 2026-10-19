from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm

def lista_projetos(views):
    projetos = Projeto.objects.all()
    return render(views, 'projetos/lista_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/form_projeto.html', {'form': form})