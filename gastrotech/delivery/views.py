from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PedidoRapidoForm
from django.db import transaction # controle de transação
from .models import ItemPedido
# Create your views here.
# Programação Defensiva:
def home_pedido_rapido(request):
    if request.method == 'POST':
        form = PedidoRapidoForm(request.POST)
        
        if form.is_valid():
            # programação defensiva:
            # ATOMICIDADE
            try:
                with transaction.atomic():
                    #1. salva o pedido
                    novo_pedido = form.save(commit=False)
                    novo_pedido.status = 'PENDENTE'
                    novo_pedido.save()
                    
                    # 2. Cria itempedido
                    prato_selecionado = form.cleaned_data['prato_escolhido']
                    ItemPedido.objects.create(
                        pedido=novo_pedido,
                        prato=prato_selecionado,
                        quantidade=1
                    )
                    
                    # Baixa de Estoque
                    if prato_selecionado.estoque > 0:
                        prato_selecionado.estoque -= 1
                        prato_selecionado.save()
                    else:
                        raise Exception("Erro de concorrência: estoque insulficiente.")   
                    
                    messages.success(request, f"Pedido #{novo_pedido.id} enviado para a cozinha!")
                    return redirect('home')
                
            except Exception as e:
                print(f"Erro na transação: {e}")
                messages.error(request, "Erro interno ao processar pedido.")
        else:
            messages.error(
                request,
                f'Pedido #{novo_pedido.id} não pode ser criado.'
            )
    else: # Fluxo GET
        form = PedidoRapidoForm()
    return render(request, 'home_pedido.html', {'form': form})
        


