from module.interface import *
from os import system
from time import sleep

system('cls')
menu('Somatórios Recursivos')

def somatorio(n: int):
    if n == 1:
        return 1
    else:
        return n + somatorio(n - 1)

while True:
    try:
        n = int(input('Qual número deseja ver o somatório? '))
    except (ValueError, TypeError):
        print('\033[31mERRO! Por favor digite um número inteiro!\033[m')
        continue
    else:
        s = somatorio(n)
        print(f'O somatório de \033[32m{n}\033[m é igual a \033[35m{s}\033[m!')
        break

sleep(2)
print('\033[36mPrograma Finalizado!\033[m')
