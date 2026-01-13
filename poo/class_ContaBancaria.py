from abc import ABC, abstractmethod

class ContaBancaria(ABC): # classe abstrata
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito Realizado no valor R$ {valor},00")
         
    def get_saldo(self): #getter
        return self.__saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass
        
class ContaCorrente(ContaBancaria): # classes concreta
    
    def __init__(self, saldo_inicial=0, 
                 taxa_operacao=1.50):
        super().__init__(saldo_inicial)
        self.__taxa_operacao = taxa_operacao
    
    def sacar(self, valor):
        custo_total = valor + self.__taxa_operacao
        if valor > 0 and self.get_saldo() >= custo_total:
            novo_saldo = self.get_saldo() - custo_total
            self._ContaBancaria__saldo = novo_saldo
            print(f"Saque de R$ {valor:.2f} realizado na C. Corrente. Saldo restante {self.get_saldo()}")
        else:
            print("Saque não realizado. Saldo insuficiente")
             
class ContaPoupanca(ContaBancaria): # classe concreta
    def __init__(self, saldo_inicial=0, 
                 taxa_juros=0.1):
        super().__init__(saldo_inicial)
        self.__taxa_juros = taxa_juros

    def sacar(self, valor):
        if valor > 0 and self.get_saldo() >= valor:
            novo_saldo = self.get_saldo() - valor
            self._ContaBancaria__saldo = novo_saldo
            print(f"Saque de R$ {valor:.2f} realizado na C. Poupança. Saldo restante {self.get_saldo()}")
        else:
            print("Saque não realizado. Saldo insuficiente")
            
    def aplicar_juros(self):
        
        juros = self.get_saldo() * self.__taxa_juros
        self.depositar(juros)
        print(f"Juros de R$ {juros},00 aplicados na Poupança!")
        
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.__contas = []
        
    def get_contas(self):
        return self.__contas
    
    def transferir(self, conta_origem_idx, conta_destino_idx, valor):
        if 0 <= conta_origem_idx < len(self.__contas) and 0 <= conta_destino_idx < len(self.__contas):
            conta_origem = self.__contas[conta_origem_idx]
            conta_destino = self.__contas[conta_destino_idx]
            
            if conta_origem.sacar(valor): # Polimorfismo
                conta_destino.depositar(valor)
                print("--- Transferência Realizada com Sucesso!")
            else:
                print("--- Trasferência Falhou (2) ---")
        else:
            print("--- Transferência Falhou (1) ----")
                
    def adicionar_conta(self, conta: ContaBancaria):
        self.__contas.append(conta)
        print(f"Conta do tipo {type(conta).__name__} adicionada para o cliente {self.nome}")

# Criando os objetos
cl_joao = Cliente("João da Silva")
# Criando contas do cliente
conta_poupanca_joao = ContaPoupanca(1000)
conta_corrente_joao = ContaCorrente()
# Adicionar a conta do cliente:
cl_joao.adicionar_conta(conta_poupanca_joao)
cl_joao.adicionar_conta(conta_corrente_joao)
# Operar sobre as contas:
conta_poupanca_joao.sacar(200)
conta_corrente_joao.depositar(500)
print("Saldo conta corrente: ", conta_corrente_joao.get_saldo())
# Transferência:
print(len(cl_joao.get_contas()))
print("Saldo conta poupança: ", conta_poupanca_joao.get_saldo())


cl_flavio = Cliente("Flávio da Silva")
cl_flavio.adicionar_conta(ContaCorrente(1000))
cl_flavio.adicionar_conta(ContaPoupanca(2000))

cl_flavio.transferir(0, 1, 500)
cl_flavio.transferir(0, 1, 1000)



