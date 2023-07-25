from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
# Create your views here.

def index(request):
    produto = Produto.objects.all()
    total_produtos = Produto.objects.count()
    total_marcas = Marca.objects.count()
    total_categorias = Categoria.objects.count()
    context = {
        'produtos' : produto,
        'total_produtos' : total_produtos,
        'total_marcas' : total_marcas,
        'total_categorias' : total_categorias
    }
    return render(request, 'index.html', context)

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
            return redirect('index')

    else:
        form = ProdutoForm()

    return render(request, 'form-produto.html', context={'form':form})

def produto_editar(request, id):
    produto = get_object_or_404(Produto,id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'form-produto.html', context={'form':form})
        

def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('index')

def produto_detalhe(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'detalhe.html', context={'produto':produto})


def categoria_criar(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoriaForm()
            return redirect('index')

    else:
        form = CategoriaForm()

    return render(request, 'form-categoria.html', context={'form':form})


def categoria_editar(request, id):
    produto = get_object_or_404(Categoria,id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CategoriaForm(instance=produto)

    return render(request, 'form-categoria.html', context={'form':form})
        

def categoria_remover(request, id):
    produto = get_object_or_404(Categoria, id=id)
    produto.delete()
    return redirect('index')


def marca_criar(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            form = MarcaForm()
            return redirect('index')

    else:
        form = MarcaForm()

    return render(request, 'form-marca.html', context={'form':form})


def marca_editar(request, id):
    produto = get_object_or_404(Marca,id=id)

    if request.method == 'POST':
        form = MarcaForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = MarcaForm(instance=produto)

    return render(request, 'form-marca.html', context={'form':form})
        

def marca_remover(request, id):
    produto = get_object_or_404(Marca, id=id)
    produto.delete()
    return redirect('index')

