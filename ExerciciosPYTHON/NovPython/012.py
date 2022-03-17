print('='*8,'Inscritos','='*8)
from module.interface import *
from time import sleep

menu('Lista de Inscritos')
with open('Inscritos.txt') as arq:
    for o, n in enumerate(arq):
        print(f'\033[35m{o + 1}\033[m \033[36m{n.title()}\033[m')
        sleep(0.4)
print('-' * 40)

while True:
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja adicionar uma pessoa? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
    with open('Inscritos.txt', 'a') as arq:
        nome = str(input('Qual o nome da pessoa? ')).strip().title()
        arq.write(f'\n{nome}')
    sleep(1.5)
    print('\033[32mPessoa adicionada com SUCESSO!\033[m')
    sleep(0.5)
print('\033[36mPrograma Finalizado!\033[m')
