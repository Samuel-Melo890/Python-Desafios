from module.interface import *
from os import system
import json

system('cls')
menu('Serialização de Dicionários em Json')

class Paladin():
    def __init__(self, nome, arma, ataque=50, defesa=50, agilidade=50):
        self.nome = nome
        self.arma = arma
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
    def atacar(self):
        print(f'\033[36m{self.nome}\033[m golpeia com \033[35m{self.arma}\033[m!')
    def defender(self):
        print(f'\033[36m{self.nome}\033[m bloqueia com \033[35m{self.arma}\033[m!')
    def esquivar(self):
        print(f'\033[36m{self.nome}\033[m esquiva!')

p1 = Paladin('Jeanne', 'Espada', 80, 60, 90)
p2 = Paladin('Skull Knight', 'Espada da Ressonancia', 90, 80, 60)

l_json = [p1.__dict__, p2.__dict__]

with open(r'C:\Users\saymu\Desktop\ExerciciosPYTHON\NovPython\030.json', 'w') as arq:
    json.dump(l_json, arq, indent = 4)

p1_json = json.dumps(p1.__dict__, indent = 4)
p2_json = json.dumps(p2.__dict__, indent = 4)

print(p1_json)
print('')
print(p2_json)
