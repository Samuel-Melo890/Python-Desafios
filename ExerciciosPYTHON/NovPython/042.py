from module.interface import menu
from os import system

system('cls')
menu('Funções: Args e Kwargs')

def func(*args):
    args = list(args)
    args[0] = 1000
    for v in args:
        print(v, end = ' ')
    print('')

func(1, 2, 3, 4, 5)

def keyw(**kwargs):
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    cidade = kwargs.get('cidade')
    print(f'{nome} tem {idade} anos e vive em {cidade}.')

keyw(nome = 'Jeanne', idade = 19, cidade = 'Orleans')
