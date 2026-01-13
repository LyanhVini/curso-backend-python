from django.shortcuts import render, get_object_or_404
from .models import Produto

def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'pagina_inicial.html', 
                  {'produtos': produtos})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhe.html', 
                  {'p': produto})