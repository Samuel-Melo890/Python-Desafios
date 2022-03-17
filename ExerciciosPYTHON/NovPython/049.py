from module.interface import *
import os
from random import randint

os.system('cls')
menu('Complemento a Orientação a Objeto')

class Pessoa():
    ano_atual = 2022
    
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    
    def info(self):
        print(f'Nome:  {self.nome}\nIdade: {self.idade} anos\nPeso:  {self.peso} kg')
    
    @classmethod
    def get_idade(cls, nome, ano_nasc, peso):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade, peso)
    
    @staticmethod
    def gera_id():
        id = randint(10000, 99999)
        return id

p = Pessoa.get_idade('Jeanne', 1322, 65)
p.info()
print(f'ID:    {p.gera_id()}')
