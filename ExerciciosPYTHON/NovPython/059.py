from module.interface import menu
from os import system
from time import sleep

system('cls')
menu('Itens Duplicados')

def duplicated(l: list|tuple):
    d_values = set(l[:])
    duplicated = len(l) - len(d_values)
    return duplicated

l = []

for n in range(1, 11):
    i = input(f'Insira o elemento {n} na lista: ').strip()
    l.append(i)

sleep(1)
print(f'\nO número de itens duplicados na lista foi de {duplicated(l)}!')
