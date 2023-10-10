from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Jogo

def home(request):
    url_params = request.GET
    search = request.GET.get('search')
    all_games = Jogo.objects.all().order_by('nome')
    page = request.GET.get('page')
    if search != '' and search is not None:
        all_games = all_games.filter(nome__icontains=search)
    paginator = Paginator(all_games, 10)
    jogos = paginator.get_page(page)

    return render(request,'index.html',{"jogos":jogos, "search":search})

def salvar(request):
    nnome = request.POST.get("nome")
    ndesc = request.POST.get("desc")
    nqtt = request.POST.get('qtt')
    npedidos = request.POST.get('pedidos')
    nprecoc = request.POST.get('preco_custo')
    nprecov = request.POST.get('preco_venda')
    Jogo.objects.create(nome=nnome, desc=ndesc, qtt=nqtt, pedidos=npedidos, preco_custo=nprecoc, preco_venda=nprecov)
    return redirect(home)

def editar(request, id):
    jogo = Jogo.objects.get(id=id)
    return render(request, 'update.html', {'jogo':jogo})

def alterar(request, id):
    nnome = request.POST.get("nome")
    ndesc = request.POST.get("desc")
    nqtt = request.POST.get('qtt')
    npedidos = request.POST.get('pedidos')
    nprecoc = request.POST.get('preco_custo')
    nprecov = request.POST.get('preco_venda')
    jogo = Jogo.objects.get(id=id)
    jogo.nome, jogo.desc, jogo.qtt, jogo.pedidos, jogo.preco_custo, jogo.preco_venda = nnome, ndesc, nqtt, npedidos, nprecoc, nprecov
    jogo.save()
    return redirect(home)

def apagar(request, id):
    jogo = Jogo.objects.get(id=id)
    jogo.delete()
    return redirect(home)

def registrar(request):
    return render(request, 'register.html')