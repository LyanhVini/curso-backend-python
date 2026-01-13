from abc import ABC, abstractmethod
from enum import Enum

class StatusItem(Enum):
    RECEBIDO = "Recebido"
    EM_PREPARO = "Em Preparo"
    PRONTO = "Pronto"

class StatusPedido(Enum):
    ABERTO = "Aberto"
    FECHADO = "Fechado"

class ItemMenu(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.__status = StatusItem.RECEBIDO
    
    def get_status(self):
        return self.__status.value
    
    def set_status(self, novo_status: StatusItem):
        self.__status = novo_status
        print(f"Status de {self.nome} alterado para: {self.get_status()}")
        
    @abstractmethod   
    def descrever(self):
        pass

class Prato(ItemMenu):
    
    def __init__(self, nome, preco, tempo_preparo):
        super().__init__(nome, preco)
        self.tempo_preparo = tempo_preparo
        
    def descrever(self):
        return f"- Prato: {self.nome} (Preparo: {self.tempo_preparo} min) [{self.get_status()} - R$ {self.preco:.2f}]"

class Bebida(ItemMenu):
    
    def __init__(self, nome, preco, tamanho_ml):
        super().__init__(nome, preco)
        self.tamanho_ml = tamanho_ml
        
    def descrever(self):
        return f"- Bebida: {self.nome} ({self.tamanho_ml}) [{self.get_status()} - R$ {self.preco:.2f}]"
    
class Pedido:
    
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self._itens = []
        self.__status = StatusPedido.ABERTO
        self.__taxa_servico = 0.10
        
    def adicionar_item(self, item: ItemMenu):
        if self.__status == StatusPedido.ABERTO:
            self._itens.append(item)
            print(f"Item adicionado ao pedido {self.id_pedido}")
        else:
            print(f"Não é possível adicionar itens a esse pedido.")
            
    def alterar_status_item(self, indice_item, novo_status: StatusItem):
        
        if 0 <= indice_item < len(self._itens):
            self._itens[indice_item].set_status(novo_status)
            print(f"Status do pedido alterado para {self.novo_status}")
        else:
            print("Item não encontrado no pedido")    
            
    def calcular_subtotal(self):
        return sum(item.preco for item in self._itens)
    
    def exibir_comanda_cozinha(self):
        print("COMANDO PARA COZINHA | Pedido: {self.id_pedido}\n")
        for item in self._itens:
            print(item.descrever())
    
    def exibir_fatura(self):
        self.__status = StatusPedido.FECHADO
        subtotal = self.calcular_subtotal()
        servico = subtotal * self.__taxa_servico
        total_a_pagar = servico + subtotal
        
        print(f"FATURA | PEDIDO: {self.id_pedido}")
        print("="*40)
        for item in self._itens:
            print(f"{item.nome} R$ {item.preco:.2f}")
        print("."*40)
        print(f"Subtotal: {subtotal}")
        print(f"Taxa de Serviço: {servico}")
        print(f"TOTAL A PAGAR: {total_a_pagar}")
        print("="*40)
        
        
# criar os itens:
moqueca = Prato("Moqueca Paraense", 85, 30)
refrigerante = Bebida("Coca Cola", 7.0, 350)
sorvete = Prato("Sorvete COP-30", 30, 300)

# abrindo pedido e adicionando itens

pedido_mesa_01 = Pedido("mesa-01")
pedido_mesa_01.adicionar_item(moqueca)
pedido_mesa_01.adicionar_item(refrigerante)
pedido_mesa_01.adicionar_item(sorvete)

# Exibir comanda:
pedido_mesa_01.exibir_comanda_cozinha()

        