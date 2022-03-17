from module.interface import menu
from os import system

system('cls')
menu('Levantando Exceções em Python')

def divide(n1: int, n2: int):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(f'\033[31mERRO! {error}\033[m')
        raise

try:
    print(divide(5, 0))
except ZeroDivisionError as erro:
    print(erro)
