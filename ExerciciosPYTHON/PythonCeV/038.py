print('='*8,'Comparando Numeros','='*8)

n1 = int(input('Digite um numero inteiro qualquer: '))
n2 = int(input('Digite outro numero inteiro qualquer: '))
if n1 > n2 :
    print('O primeiro valor e o {}MAIOR{}.'.format('\033[36m','\033[m'))
elif n2 > n1 :
    print('O segundo valor e o {}MAIOR{}.'.format('\033[36m','\033[m'))
else:
    print('Os dois valores sao {}IGUAIS{}.'.format('\033[33m','\033[m'))
