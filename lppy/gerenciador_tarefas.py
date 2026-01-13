def add_tarefa(tarefas):
    titulo = input("Digite o titulo da tarefa: ")
    tarefas.append({'titulo': titulo, 'concluida': False})

def listar_tarefas(tarefas):
    
    for i, tarefa in enumerate(tarefas):
        print(f"{i}, {tarefa}")
    
def marcar_concluida(tarefas):
    
    listar_tarefas(tarefas)
    
    num = int(input("Qual tarefa você quer marcar? "))
    tarefas[num - 1]['concluida'] = True
    print(f"Tarefa {num} foi concluída")

def sair():
    
    return False

def main():
    
    tarefas = []
    
    opcao = {
        '1': add_tarefa,
        '2': listar_tarefas,
        '3': marcar_concluida,
        '4': sair
    }
    
    continuar = True 
    while continuar:
        
        print("Menu: (1) add tarefas, (2) listar tarefas, (3) marcar concluida, (4) sair")
        escolha = input("Qual a sua escolha: ")
        
        funcao = opcao.get(escolha)
        
        if funcao:
            if funcao(tarefas) == False:
                continuar = False
        else:
            print("OPção inválida")
        
main()
    