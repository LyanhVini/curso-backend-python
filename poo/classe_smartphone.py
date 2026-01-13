class Smartphone:
    def __init__(self, marca: str, modelo: str, so: str):
        self.marca = marca
        self.modelo = modelo
        self.so = so
        self.bateria = 100
        self.ligado = False
        
    def ligar(self):
        if self.bateria > 5:
            self.ligado = True
            print(f"{self.modelo} está ligado")
        else:
            print("Bateria insulficiente!")
    
    def desligar():
        self.ligado = False
        print("O smartphone está desligando...")
    
    def fazer_chamada(self, numero: int):
        if self.ligado == True and self.bateria >= 10:
            self.bateria -= 5
            print(f"Chamando {numero}...")
        else:
            print("Não é possível realizar a chamada.")
    
    def carregar(self, porcentagem):
        self.bateria = min(100, self.bateria + porcentagem) # r = min(valor1, valor2)
        print(f"Smartphone carregado. Bateria de {self.bateria}%")
        
    def status_bateria(self):
        print(f"Bateria: {self.bateria}%")
        
phone_1 = Smartphone("Apple", "Iphone 15 PRO", "IOS 26")
phone_2 = Smartphone("Samsung", "S24 Ultra", "Android")
print("\nLigando Smartphones...\n")
phone_1.ligar()
phone_1.status_bateria()
phone_2.ligar()
phone_2.status_bateria()

# chamada
print("\nFazendo chamada...\n")
phone_1.status_bateria()
phone_1.fazer_chamada(981557788)        
phone_1.status_bateria()

# carregar
print("\nCarregando...\n")
phone_1.carregar(5)
phone_1.status_bateria()
