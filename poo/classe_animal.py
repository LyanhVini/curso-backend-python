class Animal:
    def __init__(self, especie: str, nome: str, idade: int):
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.vivo = True
        self.fome = 50
    
    def comer(self):
        if self.vivo:
            self.fome += 10
            return f"{self.nome} comeu."
        else:
            return f"O animal não pode comer"
    
    def dormir(self):
        if self.vivo and self.fome > 30:
            self.fome -= 20
            return f"{self.nome} está dormindo"
        else:
            return f"{self.nome} não pode dormir."
    
    def emitir_som(self):
        if self.vivo:
            return f"{self.nome} emite um som"
        else:
            return f"{self.nome} não pode emitir som"
    
    def mover(self):
        if self.vivo:
            return f"{self.nome} está se movendo"
        else:
            return f"{self.nome} não pode se mover"

esp = input("Qual a espécie: ")
nome = input("Qual o nome do cachorro: ")
idade = input("Qual a idade do cachorro: ")
        
cachorro1 = Animal(esp, nome, idade) 
print(cachorro1.idade)
print(cachorro1.nome)
c = cachorro1.emitir_som()
print(c)
print("Antes de comer", cachorro1.fome)
j = cachorro1.comer()
print(j)
print("Após comer: ", cachorro1.fome)

print(cachorro1.dormir())

