#precos = [50.00, 120.00, 9.99, 35.50]
#preco_aumento = list(map(lambda p: p * 1.1, precos))
                    #map(funcao, iteravel)
#for num in preco_aumento:
#    print(f"{num:.2f}")

#celsius = [0, 10, 9, 31, 27, 15, 12]                    
#fehrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
#print(fehrenheit)

#alunos = [{'nome': 'Ana', 'nota': 9.5}, 
#          {'nome': 'Beto','nota': 6.9}, 
#          {'nome': 'Carla','nota': 7.0}, 
#          {'nome': 'Davi','nota': 5.8},]

#aprovados = filter(lambda aluno: aluno['nota'] >= 7.0, alunos)
#print(list(aprovados))

vendas = [{"id": 1,"produto": "Notebook","valor": 2500.00,"status": "concluido"},
        {"id": 2, "produto": "Mouse","valor": 50.00,"status": "cancelado"},
        {"id": 3,"produto": "Teclado","valor": 120.00,"status": "concluido"},
        {"id": 4,"produto": "Monitor","valor": 800.00,"status": "pendente"},
        {"id": 5,"produto": "Headset","valor": 150.00,"status": "concluido"},
        {"id": 6,"produto": "Webcam","valor": 200.00,"status": "concluido"},
        {"id": 7,"produto": "Tablet","valor": 1200.00,"status": "cancelado"},
        {"id": 8,"produto": "Smartphone","valor": 1800.00,"status": "concluido"}]

# 1. Filtrar vendas válidas
vendas_validas = list(filter(lambda v: v["status"] == 'concluido', vendas))
print("Filtragem de Vendas Válidas: ", vendas_validas)

#2. Adicionar Imposto
def adicionar_imposto(venda):
    venda_com_imposto = venda.copy()
    venda_com_imposto["valor_com_imposto"] = venda['valor'] * 1.15
    return venda_com_imposto

vendas_com_imposto = list(map(adicionar_imposto, vendas_validas))
print("Vendas com imposto: ", vendas_com_imposto)

vendas_premium = list(filter(lambda v: v["valor_com_imposto"] > 1000, vendas_com_imposto))
print("Vendas premium: ", vendas_premium)

