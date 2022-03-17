from module.interface import menu
from os import system
from time import sleep

system('cls')
menu('Sets em Python')

def distinct(i: list|tuple):
    d_values = set(i[:])
    return d_values

l = []

for n in range(1, 6):
    i = input(f'Diga-me o item {n} da lista: ').strip()
    l.append(i)

l_dist = distinct(l)
sleep(1)
print(f'\nItems distintos da lista: {l_dist}')
