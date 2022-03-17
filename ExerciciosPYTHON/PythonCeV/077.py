print('='*8,'Contando Vogais em Tupla','='*8)
p = ('deus', 'maria', 'jose', 'anjo', 'cruzadas', 'templario', 'batalha')
for n in p:
    print(f'\nPara a palavra \033[34m{n.upper()}\033[m temos as vogais: ', end = '')
    for l in n:
        if l in 'AaEeIiOoUu':
            print(f'\033[4;36m{l.upper()}\033[m', end = ' ')
