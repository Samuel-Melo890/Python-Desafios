print('='*8,'Jogo do Par ou Ímpar','='*8)
from random import randint
from time import sleep
v = 0
while True:
    js = str(input('Escolha: Par ou Ímpar? ')).strip().title()[0]
    while js not in 'PÍI':
        js = str(input('Escolha: Par ou Ímpar? ')).strip().upper()[0]
    cn = randint(0, 5)
    jn = int(input('Escolha um número inteiro de 0 a 5: '))
    while jn < 0 or jn > 5:
        jn = int(input('Escolha um número inteiro de 0 a 5: '))
    s = cn + jn
    print('\033[35m-=-\033[m' * 16)
    print(f'O jogador escolheu {jn} e o computador escolheu {cn}!')
    print(f'A soma deu {s}.')
    if js in 'P':
        if s % 2 == 0:
            print('\033[32mO jogador venceu!\033[m')
        else:
            break
    if js in 'ÍI':
        if s % 2 == 0:
            break
        else:
            print('\033[32mO jogador venceu!\033[m')
    print('\033[35m-=-\033[m' * 16)
    print('Vamos jogar novamente...')
    sleep(1)
    v += 1
print('\033[31mVocê perdeu!\033[m')
print('\033[35m-=-\033[m' * 16)
print(f'\033[36mVitórias conquistadas:\033[m {v}')
