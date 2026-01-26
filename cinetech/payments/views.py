import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

@login_required
def criar_checkout(request):
    """Cria uma sessão de checkout no Stripe"""
    # Configurar Stripe com a chave secreta do settings.py
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    sacola = request.session.get('ingressos_selecionados', {})
    
    if not sacola:
        messages.error(request, 'Sua sacola está vazia!')
        return redirect('index')
    
    # Importar modelo Filme do app cine
    from cine.models import Filme
    
    # Criar line_items para o Stripe
    line_items = []
    for filme_id, quantidade in sacola.items():
        filme = Filme.objects.get(pk=filme_id)
        line_items.append({
            'price_data': {
                'currency': 'brl',
                'product_data': {
                    'name': f'Ingresso: {filme.nome}',
                },
                'unit_amount': int(filme.preco * 100),  # Stripe usa centavos
            },
            'quantity': quantidade,
        })
    
    try:
        # Criar sessão de checkout do Stripe
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/sucesso/'),
            cancel_url=request.build_absolute_uri('/cancelado/'),
        )
        return redirect(checkout_session.url)
    except Exception as e:
        messages.error(request, f'Erro ao criar pagamento: {str(e)}')
        return redirect('ver_sacola')

def pagamento_sucesso(request):
    """Página de sucesso após pagamento"""
    # Limpar a sacola após pagamento bem-sucedido
    if 'ingressos_selecionados' in request.session:
        del request.session['ingressos_selecionados']
        request.session.modified = True
    
    messages.success(request, '🎉 Pagamento realizado com sucesso! Seus ingressos foram confirmados.')
    return render(request, 'payments/sucesso.html')

def pagamento_cancelado(request):
    """Página quando o pagamento é cancelado"""
    messages.warning(request, 'O pagamento foi cancelado. Seus itens ainda estão na sacola.')
    return render(request, 'payments/cancelado.html')


# ============ WEBHOOK SEGURO ============
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt  # Webhooks externos não enviam CSRF token
def stripe_webhook(request):
    """
    Webhook para receber notificações do Stripe.
    O Stripe envia eventos quando pagamentos são confirmados, falham, etc.
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    
    try:
        # Verificar assinatura para garantir que veio do Stripe
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError:
        return HttpResponse('Payload inválido', status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse('Assinatura inválida', status=400)
    
    # Processar o evento
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Aqui você pode: salvar pedido no banco, enviar email, etc.
        print(f"✅ Pagamento confirmado! Session ID: {session['id']}")
    
    return HttpResponse('OK', status=200)
