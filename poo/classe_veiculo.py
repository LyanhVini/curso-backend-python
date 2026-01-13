class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"Acelerando para {self.velocidade} km/h")
    
    def frear(self, valor):
        self.velocidade = max(0, self.velocidade - valor) # max(valor1, valor2)
        print(f"Reduzindo para {self.velocidade} km/h")
        
    def info(self):
        print(f"{self.marca} - {self.modelo} - {self.ano}")
        
# super()

class Carro(Veiculo):
    def __init__(self, marca:str, modelo: str, ano: int, portas: int):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def abrir_porta(self, numero):
        print(f"Porta {numero} aberta.")
    
    def info(self):
        print(f"{super().info()} - {self.portas} portas")

class Moto(Veiculo):
    def __init__(self, marca: str, -modelo: str, ano: int, cilindradas: int):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def empinar(self):
        print("Moto empinando!")
    
    def info(self):
        print(f"{super().info()} - {self.cilindradas} cilindradas")
        
carro_1 = Carro("Tesla", "XXXY", 2025, 4)
carro_1.info()
moto_1 = Moto("Honda", "Bros", 2025, 10)
moto_1.info()

# utilizando métodos
print("\n")
carro_1.abrir_porta(3)
carro_1.acelerar(20)
carro_1.frear(10)
print(carro_1.velocidade)

print("\n")
print(moto_1.velocidade)
moto_1.acelerar(40)
moto_1.frear(10)
print(moto_1.velocidade)


# min(v1, v2) -> retorna o valor mínimo ou menor valor
# max(v1, v2) -> retorna o valor máximo ou maior valor
