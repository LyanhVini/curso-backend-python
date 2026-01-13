# Calculadora de IMC (Índice de Massa Corporal)
print("Calculadora de IMC")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print("\nResultado:")
print(f"Seu IMC é: {imc:.2f}")
print("\nClassificação (padrão OMS):")
print("IMC < 18.5: Abaixo do peso")
print("18.5 <= IMC < 25: Peso normal")
print("25 <= IMC < 30: Sobrepeso")
print("IMC >= 30: Obesidade")