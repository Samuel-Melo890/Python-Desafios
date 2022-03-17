from module.interface import *
from os import system
from time import sleep

system('cls')
menu('Fatorial Recursivo')

def fatorial(n: int):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

while True:
    try:
        n = int(input('Qual o número que deseja ver o fatorial? '))
    except (ValueError, TypeError):
        print('\033[31mERRO! Por favor insira um número inteiro válido!\033[m')
    else:
        fat = fatorial(n)
        print(f'>> O fatorial de \033[32m{n}\033[m é igual a \033[35m{fat}\033[m!')
        break

sleep(1)
print('\033[36mPrograma FInalizado!\033[m')
