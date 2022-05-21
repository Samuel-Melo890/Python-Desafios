import json
from os import system
from module.interface import *

system('cls')

menu('Carregando Arquivos Json Externos')
with open(r'C:\Users\saymu\Documents\MyRepository\Python-Desafios\ExerciciosPYTHON\NovPython\029.json', 'r') as f:
    jogador = json.load(f)
    for k, v in jogador.items():
        print(f'{k.title()}: {v}')
