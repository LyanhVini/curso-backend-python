from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PedidoRapidoForm
from .models import ItemPedido

# Esta será a nossa página inicial (Home)
def home_pedido_rapido(request):
    # --- Fluxo POST (Cliente enviou o pedido) ---
    if request.method == 'POST':
        form = PedidoRapidoForm(request.POST)
        
        if form.is_valid():
            # 1. Salva os dados do Pedido (Nome, Endereço)
            # O commit=False cria o objeto na memória, mas não salva no banco ainda.
            novo_pedido = form.save(commit=False)
            novo_pedido.status = 'PENDENTE' # Força o status inicial
            novo_pedido.save() # Agora salva de verdade no banco e gera o ID.
            
            # 2. Recupera o prato que o cliente selecionou no dropdown extra
            prato_selecionado = form.cleaned_data['prato_escolhido']
            
            # 3. Cria a ligação (ItemPedido)
            # "Este novo pedido contém 1 unidade deste prato selecionado"
            ItemPedido.objects.create(
                pedido=novo_pedido,
                prato=prato_selecionado,
                quantidade=1 # Simplificação: pedido rápido é sempre 1 item
            )
            
            # Feedback e Reset
            messages.success(request, f"Pedido #{novo_pedido.id} enviado para a cozinha! Aguarde.")
            return redirect('home')
            
        else:
             messages.error(request, "Ops! Verifique os dados informados.")
             
    # --- Fluxo GET (Cliente acessou a página) ---
    else:
        form = PedidoRapidoForm()

    return render(request, 'delivery/home_pedido.html', {'form': form})