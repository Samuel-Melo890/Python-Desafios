from module.interface import *
from os import system
from collections import deque

system('cls')
menu('Duas Filas')

def fila_chegada(l: list|tuple):
    fila = deque()
    
    for p in l:
        if p != 'Samuel':
            fila.append(p)
    
    return fila

l_chegada = ['Jeanne', 'Astolfo', 'Skull Knight', 'Guts', 'Samuel']

fila = fila_chegada(l_chegada)
ordem = []

for p in fila:
    ordem.append(p)

print('Ordem para embarcar no Ônibus:')
for o, p in enumerate(ordem):
    print(f'    {o + 1} - {p}')
