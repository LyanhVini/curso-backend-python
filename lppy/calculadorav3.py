print("===================================")
print("===   SUPER CALCULADORA   ===")
print("===================================")
print("Operações disponíveis:")
print("+ (soma), - (subtração), * (multiplicação), / (divisão)")
print("** (potenciação), // (divisão inteira), % (resto da divisão)")
print()

# 2. ENTRADA DE DADOS
numero1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação desejada: ")
numero2 = float(input("Digite o segundo número: "))

print("-----------------------------------")

# Flag para controlar se o cálculo foi bem-sucedido. Inicia como True.
calculo_sucesso = True
resultado = 0

# 3. LÓGICA CONDICIONAL E CÁLCULOS
if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '**':
    resultado = numero1 ** numero2
elif operador == '/':
    if numero2 == 0:
        print("ERRO: Divisão por zero não é permitida.")
        calculo_sucesso = False # O cálculo falhou
    else:
        resultado = numero1 / numero2
elif operador == '//':
    if numero2 == 0:
        print("ERRO: Divisão inteira por zero não é permitida.")
        calculo_sucesso = False # O cálculo falhou
    else:
        resultado = numero1 // numero2
elif operador == '%':
    if numero2 == 0:
        print("ERRO: Módulo por zero não é permitido.")
        calculo_sucesso = False # O cálculo falhou
    else:
        resultado = numero1 % numero2
else:
    # Se o operador não for nenhum dos anteriores, é inválido.
    print(f"ERRO: Operador '{operador}' é inválido.")
    calculo_sucesso = False # O cálculo falhou

# 4. EXIBIÇÃO DO RESULTADO E ANÁLISE BÔNUS
if calculo_sucesso:
    # Primeiro, exibe o resultado principal
    print(f"O resultado de {numero1} {operador} {numero2} é: {resultado}")
    print("\n--- Análise do Resultado ---")
    
    # Verifica se é positivo, negativo ou zero
    if resultado > 0:
        print("-> O resultado é um número POSITIVO.")
    elif resultado < 0:
        print("-> O resultado é um número NEGATIVO.")
    else: # Se não for maior nem menor, só pode ser zero
        print("-> O resultado é ZERO.")
        
    # Verifica se o resultado é um número inteiro antes de checar se é par ou ímpar
    if resultado == int(resultado):
        if resultado % 2 == 0:
            print("-> O resultado é um número PAR.")
        else:
            print("-> O resultado é um número ÍMPAR.")
    else:
        print("-> O resultado não é um número inteiro (possui casas decimais).")

print("-----------------------------------")
print("Fim do programa.")