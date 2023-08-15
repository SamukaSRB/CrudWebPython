from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produtos
from .forms import ProdutoForm

# Etapa site
def home(request):
    return render(request,'page/inicio.html')

def painel(request):  
    return render(request,'page/painel.html')

def produtos(request):
    produtos = Produtos.objects.all()
    print(produtos)
    return render(request,'produtos/index.html', {'produtos': produtos})

# Etapa produto
def cad_produto(request):
    formulario = ProdutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('produtos')
    return render(request, 'produtos/create.html', {'formulario': formulario})

def editar_produto(request, idProdut):
    produtos = Produtos.objects.get(idProdut=idProdut)
    formulario = ProdutoForm(request.POST or None, request.FILES or None, instance=produtos)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect ('produtos')
    return render(request, 'produtos/editar.html', {'formulario':formulario})

def deletar_produto(request, idProdut):
    produtos = Produtos.objects.get(idProdut=idProdut)
    produtos.delete()
    return redirect('produtos')


