print('='*8,'Calculos Matematicos','='*8)
n = int(input('Digite um numero inteiro qualquer:'))
print('''Analisando o valor {}, vemos que:
-Seu dobro e {}.
-Seu triplo e {}.
-Sua raiz quadrada e {:.2f}.'''.format(n,n*2,n*3,n**(1/2)))

from math import sqrt
n2 = int(input('Digite um outro numero inteiro qualquer:'))
print('''Analisando o valor {}, vemos que:
-Seu dobro e {}.
-Seu triplo e {}.
-Sua raiz quadrada e {:.2f}.'''.format(n2,n2*2,n2*3,sqrt(n2)))
