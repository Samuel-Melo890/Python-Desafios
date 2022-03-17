from module.interface import *
from os import system

system('cls')
menu('Desempacotamento de Listas')

l = ['Samuel', 'Jeanne', 'Noelle', 1, 1, 2, 3, 4]
n1, n2, n3, *outra_lista= l
print(n1, n2, n3, outra_lista)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 100]
print(*lista)
