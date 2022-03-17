print('='*8,'Jogo de Dados em Python','='*8)
from random import randint
from time import sleep
from operator import itemgetter
dado = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
print('-=' * 25)
for k, v in dado.items():
    print(f'O \033[36m{k}\033[m jogou o dado e tirou \033[32m{v}!\033[m')
    sleep(1.5)
print('-=' * 25)
rank = dict()
rank = sorted(dado.items(), key = itemgetter(1), reverse = True)
for p, k in enumerate(rank):
    print(f'Em {p + 1} lugar: \033[36m{k[0]}\033[m com \033[32m{k[1]}\033[m pontos!')
