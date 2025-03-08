from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Produto
# Create your views here.
def pagina_inicial(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        return render(request, 'pagina_inicial.html', {'produtos': produtos})

def cadastro_produto(request):
    if request.method == "GET":
        return render(request, 'cadastro_produto.html')
    elif request.method == "POST":
        nome_produto = request.POST.get('produto')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')

        produto = Produto(
            nome_produto = nome_produto,
            quantidade = quantidade_estoque,
            preco = preco,
            descricao = descricao
        )

        produto.save()

        return redirect('pagina_inicial')