from module.interface import *
from os import system

system('cls')

print('='*8,'Herança Forma','='*8)

class Forma():
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, lado1, lado2):
        super().__init__(0, 0)
        self.lado1 = lado1
        self.lado2 = lado2
    def calcularArea(self):
        self.area = self.lado1 * self.lado2
        return f'{self.area} cm²'
    def calcularPerimetro(self):
        self.perimetro = self.lado1 + self.lado2
        return f'{self.perimetro} cm'

class Triangulo(Forma):
    def __init__(self, lado1, lado2, lado3, altura):
        super().__init__(0, 0)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura = altura
    def calcularArea(self):
        l = [self.lado1, self.lado2, self.lado3]
        base = max(l)
        self.area = (base * self.altura) / 2
        return f'{self.area} cm²'
    def calcularPerimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return f'{self.perimetro} cm'

r = Retangulo(10, 20)
t = Triangulo(10, 12, 15, 13)

titulo('Formatos')

print(f'O objeto \033[35mr\033[m é da classe Forma?   {isinstance(r, Forma)}')
print(f'O objeto \033[35mr\033[m é um retângulo?      {isinstance(r, Retangulo)}')
print(f'O objeto \033[35mt\033[m é da classe Forma?   {isinstance(t, Forma)}')
print(f'O objeto \033[35mt\033[m é um triângulo?      {isinstance(t, Triangulo)}')
print('')

print(f'Área de r: {r.calcularArea()}')
print(f'Área de t: {t.calcularArea()}')
print('')
print(f'Perímetro de r: {r.calcularPerimetro()}')
print(f'Perímetro de t: {t.calcularPerimetro()}')
