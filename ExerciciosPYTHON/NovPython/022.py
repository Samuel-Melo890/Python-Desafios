from os import system
from module.interface import *

system('cls')

print('='*8,'Filtro dos Pares e Ímpares','='*8)

numeros = []

for c in range(0, 10):
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)

pares = filter(lambda v: v % 2 == 0, numeros)
impares = filter(lambda v: v % 2 != 0, numeros)

titulo('Lista dos Pares')
for v in pares:
    print(f'\033[35m{v}\033[m', end = ', ')
print('')

titulo('Lista do Ímpares')
for v in impares:
    print(f'\033[35m{v}\033[m', end = ', ')
print('')
