from module.interface import *
from os import system

system('cls')
menu('Parênteses Pilhas')

f = input('Digite uma frase com parênteses: ').strip()
cont = 0
pilha = []

while cont < len(f):
    if f[cont] == '(':
        pilha.append('(')
    elif f[cont] == ')':
        if len(pilha) != 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    
    cont += 1

if pilha != []:
    print('\033[31mSeus parênteses foram colocados de forma errada!\033[m')
else:
        print('\033[32mOs parênteses foram colocados corretamente!\033[m')
