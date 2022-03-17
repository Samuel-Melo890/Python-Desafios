from module.interface import *
from os import system

system('cls')

print('='*8,'Herança de Atleta','='*8)

class Atleta():
    def __init__(self, peso, aposentado=False):
        self.peso = peso
        self.aposentado = aposentado
    def aposentar(self):
        self.aposentado = True
        print('Atleta está aposentado agora.')
    def aquecer(self):
        print('Atleta está treinando e se aquecendo...')

class Corredor(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def correr(self):
        print('Corredor está correndo...')

class Nadador(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def nadar(self):
        print('Nadador está nadando...')

class Ciclista(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def pedalar(self):
        print('Ciclista está pedalando...')

class Triatleta(Nadador, Corredor, Ciclista):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)

at = Atleta(65)
cor = Corredor(70)
nad = Nadador(55)
cic = Ciclista(81)
tri = Triatleta(84)

system('cls')
titulo('Atleta')
print(f'Peso: {at.peso} kg')
print(f'Aposentado: {at.aposentado}')
at.aquecer()
system('pause')

system('cls')
titulo('Corredor')
print(f'Peso: {cor.peso} kg')
print(f'Aposentado: {cor.aposentado}')
cor.aquecer()
cor.correr()
system('pause')

system('cls')
titulo('Nadador')
print(f'Peso: {nad.peso} kg')
print(f'Aposentado: {nad.aposentado}')
nad.aquecer()
nad.nadar()
system('pause')

system('cls')
titulo('Ciclista')
print(f'Peso: {cic.peso} kg')
print(f'Aposentado: {cic.aposentado}')
cic.aquecer()
cic.pedalar()
system('pause')

system('cls')
titulo('Triatleta')
tri.aposentar()
print(f'Peso: {tri.peso} kg')
print(f'Aposentado: {tri.aposentado}')
tri.aquecer()
tri.correr()
tri.nadar()
tri.pedalar()
system('pause')

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
