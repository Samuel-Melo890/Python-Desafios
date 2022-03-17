print('='*8,'Jogo da Adivinhação v2.0','='*8)

from random import randint
c = randint(0, 10)
t = 0
j = 11
print('''Olá eu sou o seu Computador...\nAcabei de pensar em um número de 0 a 10.\nVocê consegue advinhar esse número?''')
while j != c:
    j = int(input('Tente adivinhar: '))
    t += 1
    if j != c:
        print('Você {}ERROU{}!!! Tente de novo!'.format('\033[31m', '\033[m'))
        if j > c:
            print('O número é menor do que isso!')
        else:
            print('O número é maior do que isso!')
print('Parabéns você conseguiu acertar o número {} depois de {} tentativas! Ha ha ha!!!'.format(c, t))
