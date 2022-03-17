from module.interface import *
import json
from os import system
from time import sleep

jogador_json = '{"nome":"Jeanne", "time":"Franca", "viva":"False", "energia":100, "equipamentos":["Espada", "Bandeira", "Crucifixo"], "cavalos":[{"cor": "Branca", "velocidade": 30}, {"cor": "Preta", "velocidade": 40}, {"cor": "Marrom", "velocidade": 35}]}'

jogador = json.loads(jogador_json)

system('cls')
menu('String Json Carregado')

cont = 0
for k, v in jogador.items():
    if cont == 4:
        print(f'\033[35m{k.title()}:\033[m {v[0]}, {v[1]}, {v[2]}')
    elif cont == 5:
        print(f'\033[35m{k.title()}:\033[m {v[0]}, \n\t {v[1]}, \n\t {v[2]}')
    else:
        print(f'\033[35m{k.title()}:\033[m {v}')
    sleep(0.5)
    cont += 1
