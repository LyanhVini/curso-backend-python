print("======== BEM VINDO AO SUPERMERCADO =========")

carrinho = []

print("COMANDOS DISPONÍVEIS: [adicionar], [listar] e [finalizar]") 

comando = input("O que você deseja fazer? ").lower()

print(type(comando))

if comando == "finalizar":

    print("Finalizando a compra...")
    breakpoint

elif comando == "adicionar":
    
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = input(f"Digite o preço de {nome_produto}")
    
    produto = {
        "nome": nome_produto,
        "preco": preco_produto
    }
    
    carrinho.append(produto)
    
    print(f"Produto {nome_produto} adicionado ao carrinho!")
    print(carrinho)

elif comando == "listar":
    
    if len(carrinho) == 0:
        print("O carrinho está vazio!")  
    else:
        print("Total de itens: ", len(carrinho)) 
        print(carrinho) 
        
else: 
    print("Comando inválido!")
    
    

    
    
    
    
    
    
    
        

    
     
    




    