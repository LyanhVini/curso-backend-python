from abc import ABC, abstractmethod
from math import pi

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area():
        pass
    @abstractmethod
    def calcular_perimetro():
        pass
    
class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
        
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * pi * self.raio
    
class Quadrado(Retangulo):
    def __init__(self):
        super().__init__(lado, lado)

def gerar_relatorio(formas): #[forma1, forma2, forma3]
    
    print("RELATÓRIO DE FORMAS GEOMÉTRICAS")
    
    for i, forma in enumerate(formas):
        
        area = forma.calcular_area()
        p = forma.calcular_perimetro()
        print(forma)
        print(f"Área: {area}, Perímetro: {p}")    
    
    area_tot = sum(forma.calcular_area for forma in formas)
    p_tot = sum(forma.calcular_perimetro for forma in formas)
    
    print(f"ÁREA TOTAL: {area_tot}, PERÍMETRO TOTAL: {p_tot}")    
    
    
# Retangulo

r = Retangulo(10, 20)
a_retangulo = r.calcular_area()
p_retangulo = r.calcular_perimetro()
print(a_retangulo)
print(p_retangulo)

c = Circulo(10)
a_circulo = c.calcular_area()
p_circulo = c.calcular_perimetro()
print(a_circulo)
print(p_circulo)

#y = [r, c]

#gerar_relatorio(l)

