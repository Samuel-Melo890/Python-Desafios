from module.interface import *
from os import system

system('cls')
menu('List Comprehension em Python')

titulo('Números')
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)

print('')
titulo('Pares')
par = [p for p in num if p % 2 == 0]
print(par)

print('')
titulo('Ímpares')
impar = [i for i in num if i % 2 != 0]
print(impar)

print('')
titulo('Modificações')
mod = [m if m != 5 else 500 for m in num ]
print(mod)

print('')
titulo('Linhas e Colunas')
l_c = [
    (x, y)
    for x in range(1, 11)
    for y in range(1, 6)
]
print(l_c)

print('')
titulo('Strings')
frase = 'Olá Otávio, como está?'
l = [letra for letra in frase]
print(l)

print('')
titulo('Listas')
nomes = ['Samuel', 'Jeanne', 'José', 'Lloyd', 'Ana', 'Veda']
n = [nome if not nome[-1] else (nome[0:-1].lower() + nome[-1].upper()) for nome in nomes]
print(n)

print('')
titulo('Lista Própria')
l_num = [numero for numero in range(0, 11)]
print(l_num)
