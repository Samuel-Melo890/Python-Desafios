print('='*8,'Sorteando Uma Ordem na Lista','='*8)
n1 = input('Nome do aluno:')
n2 = input('Nome do aluno:')
n3 = input('Nome do aluno:')
n4 = input('Nome do aluno:')
from random import shuffle
l = [n1,n2,n3,n4]
shuffle(l)
print('''A ordem de apresentacao dos alunos sera:
{}'''.format(l))
