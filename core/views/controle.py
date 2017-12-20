from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models.controle import Conta, Categoria
from core.forms.formulario import ContaForm, CategoriaForm


def inicio (request):
    dados = {}
    dados['lista_conta'] = Conta.objects.all()
    return render(request, 'core/lista_conta.html', dados)


def delete_conta(request, pk):
    dados = Conta.objects.get(id=pk)
    dados.delete()
    return redirect('inicio')

def atualizar_conta(request, pk):
    dados = {}
    conta = Conta.objects.get(id=pk)
    dados['form'] = ContaForm(instance=conta)
    dados['pk'] = pk
    return render(request, 'core/atualizar_conta.html', dados)

def conta_atualizada(request):
    conta = Conta.objects.get(pk=request.POST['id_conta'])
    form = ContaForm(request.POST or None, instance=conta)
    if form.is_valid:
        form.save()
        return redirect('inicio')

def nova_conta(request):
    dados = {}
    dados['form'] = ContaForm
    conta = ContaForm(request.POST)
    if conta.is_valid():
        conta.save()
        return redirect('inicio')
    return render(request, 'core/nova_conta.html',dados)

def conta_criada(request, pk):
    conta = Conta.objects.get(pk=pk)
    conta = ContaForm(request.POST or None, instance=conta)
    if conta.is_valid():
        conta.save()
    return redirect('inicio')


def lista_categoria(request):
    dados = {}
    dados['lista_categoria'] = Categoria.objects.all()
    return render(request, 'core/lista_categoria.html', dados)

def novaCategoria(request):
    dados={}
    dados['form'] = CategoriaForm
    categoria = CategoriaForm(request.POST)
    if categoria.is_valid():
        categoria.save()
        return redirect('inicio')
    return render(request, 'core/nova_categoria.html', dados)

def categoria_criada(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria = CategoriaForm(request.POST or None, instance=categoria)
    if categoria.is_valid():
        categoria.save()
    return redirect('lista_categoria')

def editar_categoria(request, pk):
    dados = {}
    categoria = Categoria.objects.get(id=pk)
    dados['form'] = CategoriaForm(instance=categoria)
    dados['pk'] = pk
    return render(request, 'core/editar_categoria.html', dados)



def categoria_editada(request,pk):
    categoria = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
    return redirect('lista_categoria')

def deletar_categoria(request,pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return redirect('lista_categoria')
