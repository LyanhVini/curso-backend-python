from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Filme
from .forms import EspectadorForm
# Create your views here.

# Sessão do Carrinho
def adicionar_ao_pedido(request, filme_id):
    sacola = request.session.get('ingressos_selecionados', {})

    filme_id_str = str(filme_id)
    sacola[filme_id_str] = sacola.get(filme_id_str, 0) + 1

    request.session['ingressos_selecionados'] = sacola
    request.session.modified = True
    messages.success(request, "Adicionado a Sacola!")
    return redirect('index')

def limpar_sacola(request):
    if 'ingressos_selecionados' in request.session:
        del request.session['ingressos_selecionados']
    return redirect('ver_sacola')

# Rascunho & Checkout 
def ver_sacola(request):
    
    sacola = request.session.get('ingressos_selecionados', {})
    filmes_obj = []
    total = 0
    
    for f_id, qtd in sacola.items():
        filme = get_object_or_404(Filme, pk=f_id)
        subtotal = filme.preco * qtd
        total += subtotal
        filmes_obj.append({'filme': filme,
                           'quantidade': qtd,
                           'subtotal': subtotal})
    
    if request.method == 'POST':
        request.session['rascunho_dados'] = request.POST
        request.session.modified = True
        form = EspectadorForm(request.POST)
        messages.info(request, "Rascunho salvo!")
    else:
        dados_salvos = request.session.get('rascunho_dados')
        form = EspectadorForm(dados_salvos)
        
    return render(request,
                  'sacola.html',
                  {'itens': filmes_obj,
                   'total': total,
                   'form': form})
    
# Controle de Acesso
def index(request):
    filmes = Filme.objects.all()
    qtd = len(request.session.get('ingressos_selecionados', {}))
    return render(request, 'index.html',
                  {'filmes': filmes,
                   'qtd': qtd})

@login_required
def finalizar_pedido(request):
    sacola = request.session.get('ingressos_selecionados', {})

    if not sacola:
        messages.error(request, 'Sua sacola está vazia!')
        return redirect('index')
    
    del request.session['ingressos_selecionados']
    request.session.modified = True
    return redirect('index')
    
    