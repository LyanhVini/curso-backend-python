print("------ CALCULADORA DESCONTOS --------")

preco = float(input("Informe o preço do produto: "))
porcentagem = float(input("Informa o desconto desse produto (15 para 15%): ")) 

valor_desconto = (preco * porcentagem) / 100
preco_final = preco - valor_desconto

print(f"O valor do desconto é: {valor_desconto}")
print(f"O preço final do produto é: R$ {preco_final:.2f}")




