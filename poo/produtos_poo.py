class Produto:
    
    def __init__(self, nome: str, preco: float, estoque: int):
        # RF01
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        print(f"Produto {self.nome} criado com o preço R$ {self.preco} e estoque de {self.estoque} unidades")
        
        def aplicar_desconto(self, percent_desconto: float):
            # RF02
            desconto = self.preco * (percent_desconto / 100)
            novo_preco = self.preco - desconto
            
            # RFN01
            if novo_preco < 0:
                self.preco = 0.0
                print(f"[INFO] Desconto {percent_desconto} aplicado em {self.nome}.")
            else:
                self.preco = novo_preco
                print(f"[INFO] Desconto de {percent_desconto} aplicado em {self.nome}")
        
        # RF03
        def verificar_estoque(self):
            return self.estoque > 0
        

# 1. Cria um objeto
notbook = Produto('Notbook', 4000, 10)
celular1 = Produto('Iphone 17', 17000, 10)
celular2 = Produto('Iphone 15', 3500, 10)
celular3 = Produto('Iphone 13', 2500, 10)
celular4 = Produto('Iphone 12', 1500, 10)
print(notbook.nome)

# 2. Teste de verificação de stoque
print(f"O produto {notbook.nome} está em estoque? {'Sim' if celular3.verificar_estoque() else 'Não'}")
