from os import system
from module.interface import *

system('cls')

print('='*8,'Herança Ingresso','='*8)

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        return f'R${self.valor},00'

class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional
    def imprimeValor(self):
        v = self.valor + self.adicional
        return f'R${v},00'

ingresso = Ingresso(10)
ingresso_vip = Vip(10, 15)

titulo('Ingressos Para O Show')
print(f'Ingresso normal...{ingresso.imprimeValor()}')
print(f'Ingresso vip......{ingresso_vip.imprimeValor()} ')
