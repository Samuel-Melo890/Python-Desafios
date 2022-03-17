print('='*8,'Pedra, Papel ou Tesoura','='*8)

print('''Escolha uma opcao para jogar:
[0] Pedra
[1] Papel
[2] Tesoura''')
j = int(input('Opcao escolhida: '))
l = ['Pedra','Papel','Tesoura']
from random import choice
c = choice(l)

from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(0.5)

print('-=-'*9)
print('O jogador jogou {}!'.format(l[j]))
print('O computador jogou {}!'.format(c))
print('-=-'*9)

if j == 0:
    if c == l[0]:
        print('{}Empate!{}'.format('\033[33m','\033[m'))
    elif c == l[1]:
        print('{}O jogador perdeu!{}'.format('\033[31m','\033[m'))
    else:
        print('{}O jogador venceu!{}'.format('\033[32m','\033[m'))
elif j == 1:
    if c == l[0]:
        print('{}O jogador venceu!{}'.format('\033[32m','\033[m'))
    elif c == l[1]:
        print('{}Empate!{}'.format('\033[33m','\033[m'))
    else:
        print('{}O jogador perdeu!{}'.format('\033[31m','\033[m'))
elif j == 2:
    if c == l[0]:
        print('{}O jogador perdeu!{}'.format('\033[31m','\033[m'))
    elif c == l[1]:
        print('{}O jogador venceu!{}'.format('\033[32m','\033[m'))
    else:
        print('{}Empate!{}'.format('\033[33m','\033[m'))
else:
    print('{}Opcao invalida!{}'.format('\033[31m','\033[m'))
