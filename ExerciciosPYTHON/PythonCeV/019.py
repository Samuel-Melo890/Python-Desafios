print('='*8,'Sorteando Um Item na Lista','='*8)
n1 = input('Nome do aluno:')
n2 = input('Nome do aluno:')
n3 = input('Nome do aluno:')
n4 = input('Nome do aluno:')
from random import choice
l = [n1,n2,n3,n4]
a = choice(l)
print('O aluno sorteado para apagar o quadro foi {}'.format(a))
