def adicionar_tarefa(tarefas):
    titulo = input("Digite o seu título: ")
    tarefas.append({'titulo': titulo,
                    'concluida': False})
    print(f'Tarefa "{titulo}" adicionada.')

def listar_tarefas(tarefas):
    
    for i, tarefas in enumerate(tarefas, start=1): 
        status = "X" if tarefas['concluida'] else " " 
        print(f"{i}. [{status}] - {tarefas['titulo']}")
    print("---------------------------------")
    
def marcar_tarefas(tarefas):
    try:
        listar_tarefas(tarefas)
        n = int(input("Qual tarefa marcar como concluída: "))
        tarefas[n - 1]['concluida'] = True
        print(f"Tarefa {n} concluída") 
    except (ValueError, IndexError):
        print("ERRO: número inválido")

def sair(tarefas):
    print("Saindo do programa...")
    return False
    
def main():
    
    tarefas = []
    continuar = True
    
    opcoes = {
        '1': adicionar_tarefa,
        '2': listar_tarefas,
        '3': marcar_tarefas,
        '4': sair
    }
    
    while continuar:
        
        print("Menu: \n1. Adicionar\n2. Listar\n3. Marcar Concluída\n4. Sair")
        
        escolha = input("O que deseja fazer? ")
        
        funcao = opcoes.get(escolha)
        
        if funcao:
            if funcao(tarefas) == False:
                continuar = False
        else:
            print("Opção Inválida.")
            
main()
            




