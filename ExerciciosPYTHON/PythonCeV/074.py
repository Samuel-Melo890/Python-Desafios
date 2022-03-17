print('='*8,'Maior e Menor Valores em Tupla','='*8)
from random import randint
a = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
print('Os valores sorteados foram:')
for n in a:
    print(f'\033[36m{n}\033[m', end = ' ')
maior = max(a)
menor = min(a)
print(f'\nO maior valor randomizado foi \033[4;32m{maior}\033[m e o menor, \033[4;33m{menor}\033[m.')
