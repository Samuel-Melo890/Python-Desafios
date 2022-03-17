print('='*8,'Par ou Impar?','='*8)

n = int(input('Diga-me um numero inteiro qualquer: '))
if n%2==0:
    print('O numero {} e {}PAR{}!'.format(n,'\033[4;36m','\033[m'))
else:
    print('O numero {} e {}IMPAR{}!'.format(n,'\033[4;36m','\033[m'))
