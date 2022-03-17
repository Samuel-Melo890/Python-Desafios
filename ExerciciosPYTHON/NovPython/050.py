from module.interface import *
from os import system

system('cls')
menu('Complemento a Orientação a Objeto 2')

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, porc):
        porc = porc / 100; desc = self.preco * porc
        self.preco = self.preco - desc
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('Woye', 'R$100')
p1.desconto(10)
print(p1.preco)
