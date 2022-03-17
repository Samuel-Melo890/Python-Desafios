print('='*8,'Jogo da Adivinhacao v 1.0','='*8)

print('\033[1;36m=-'*22+'=\033[m')
print('''{}Bem Vindo ao Jogo da Adivinhacao!!!
Pense em um numero entre 0 e 5 para comecar!{}'''.format('\033[1;32m','\033[m'))
print('\033[1;36m''=-'*22+'=''\033[m')

from random import randint
c = randint(0,5)
n = int(input('Escolha um numero entre 0 e 5:'))
from time import sleep
print('Processando...')
sleep(2)
if c==n:
    print('{}Parabens voce venceu o desafio! Voce acertou o numero!{}'.format('\033[32m','\033[m'))
else:
    print('{}Voce perdeu!!! O numero escolhido era {}!{}'.format('\033[31m',c,'\033[m'))
    