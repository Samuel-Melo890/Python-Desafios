print('='*8,'Palpites Para a Mega Sena','='*8)
from random import randint
from time import sleep
qj = int(input('Quantos jogos serão gerados? '))
l = []
l1 = []
for c in range(0, qj):
    while True:
        n = randint(1, 60)
        if n not in l1:
            l1.append(n)
        if len(l1) == 6:
            l1.sort()
            l.append(l1[:])
            l1.clear()
            break
for o, j in enumerate(l):
    print(f'O jogo número {o + 1} fica : {j}')
    sleep(1)
print(f'{" < Boa Sorte > ":=^45}')
