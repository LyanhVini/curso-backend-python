from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Participante, ProdutoLoja, Venda
from .serializers import ParticipanteSerializer, ProdutoSerializer, VendaSerializer

# API PÚBLICA (Validação de Ingresso) 
@api_view(['GET'])
def validar_ingresso(request, codigo):
    participante = get_object_or_404(Participante, codigo_ingresso=codigo)
    return Response({
        "valido": True,
        "participante": participante.nome,
        "categoria": "VIP" if participante.vip else "Standard"
    })

# API INTERNA (Consulta de Preço)
@api_view(['GET'])
def consultar_preco(request, ean):
    produto = get_object_or_404(ProdutoLoja, codigo_barras=ean)
    serializer = ProdutoSerializer(produto)
    return Response(serializer.data)

# DASHBOARD (Agregação de Dados) 
@api_view(['GET'])
def dashboard_dados(request):
    faturamento = Venda.objects.aggregate(
        total=Sum(F('produto__preco') * F('quantidade'))
    )['total'] or 0

    # Top Produtos (Anotação / Group By)
    top_produtos = Venda.objects.values('produto__nome')\
        .annotate(total_vendido=Sum('quantidade'))\
        .order_by('-total_vendido')[:5]

    return Response({
        "kpi_faturamento": faturamento,
        "grafico": {
            "labels": [item['produto__nome'] for item in top_produtos],
            "data": [item['total_vendido'] for item in top_produtos]
        }
    })

# RELATÓRIO PDF 
def gerar_cracha(request, codigo):
    """Gera crachá em PDF simples usando ReportLab."""
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from io import BytesIO
    
    participante = get_object_or_404(Participante, codigo_ingresso=codigo)
    
    # Criar PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    # Conteúdo
    p.setFont("Helvetica-Bold", 24)
    p.drawString(100, 750, "TechSummit 2026")
    
    p.setFont("Helvetica", 18)
    p.drawString(100, 700, f"Nome: {participante.nome}")
    p.drawString(100, 670, f"Tipo: {'VIP' if participante.vip else 'Standard'}")
    p.drawString(100, 640, f"ID: {participante.codigo_ingresso}")
    
    p.save()
    buffer.seek(0)
    
    return HttpResponse(buffer.getvalue(), content_type='application/pdf')

# OTIMIZAÇÃO (Performance N+1) 
@api_view(['GET'])
def listar_vendas_otimizadas(request):
    # O select_related faz um JOIN SQL, evitando queries repetidas
    vendas = Venda.objects.select_related('produto').all().order_by('-data')[:20]
    
    serializer = VendaSerializer(vendas, many=True)
    return Response(serializer.data)