def somar(v1, v2):
    return v1 + v2

def subtrair(v1, v2):
    return v1 - v2

def divisao(v1, v2):
    
    if v2 == 0:
        print("Não existe divisão por zero")
        return None
    return v1 / v2

def multiplicacao(v1, v2):
    return v1 * v2

def menu():
    print("O que deseja fazer?")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Dividir")
    print("4 - Multiplicar")
    
def obter_numeros():
    num1 = int(input("Qual seu 1° número: "))
    num2 = int(input("Qual seu 2° número: "))
    
    return num1, num2

def main():
    
    menu()
    op = input("Qual opção você deseja?")
    num1, num2 = obter_numeros()
    match op:
        case '1':
            r = somar(num1, num2)
            print(r)
        case '2':
            r = subtrair(num1, num2)
            print(r)
        case '3':
            r = divisao(num1, num2)
            print(r)
        case '4':
            r = multiplicacao(num1, num2)
            print(r)

main()