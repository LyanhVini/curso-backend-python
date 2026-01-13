print("--- Calculadora de Descontos ---")

preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (ex: 15 para 15%): "))

valor_desconto = (preco_original * percentual_desconto) / 100

preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("\n--- Resultado ---")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto de {percentual_desconto}%: R$ {valor_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")