from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Produto
# Create your views here.
def pagina_inicial(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        produtos_count = Produto.objects.count()
        return render(request, 'pagina_inicial.html', {'produtos': produtos, 'produtos_count': produtos_count})

def cadastro_produto(request):
    if request.method == "GET":
        return render(request, 'cadastro_produto.html')
    elif request.method == "POST":
        quantidade_maxima_produtos = Produto.objects.count()
        if quantidade_maxima_produtos >= 12:
            return redirect('pagina_inicial')
        else:
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
    
def deletar_produto(request):
    ids_selecionados = request.GET.get('ids')

    if ids_selecionados:
        ids_lista = ids_selecionados.split(",")
        Produto.objects.filter(id__in=ids_lista).delete()
    
    return redirect('pagina_inicial')

def produto_perfil(request):
    id_produto = request.GET.get('id')
    
    produto = Produto.objects.get(id=id_produto)
    return render(request, 'produto_perfil.html', {'produto': produto})

def editar_produto(request, id):
    if request.method == "POST":
        produto = Produto.objects.get(id=id)

        produto.nome_produto = request.POST.get('produto')
        produto.quantidade = request.POST.get('quantidade_estoque')
        produto.preco = request.POST.get('preco')
        produto.descricao = request.POST.get('descricao')

        produto.save()
        return redirect('pagina_inicial')