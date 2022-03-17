print('='*8,'Sequência de Fibonacci v1.0','='*8)

n = int(input('Digite a quantidade de termos que quer ver na sequência de Fibonacci: '))
t1 = 0
t2 = 1
print('{} => {} => '.format(t1, t2), end = '')
c = 3
while c <= n:
    t = t1 + t2
    t1 = t2
    t2 = t
    print('{}'.format(t), end = ' => ')
    c += 1
print('Fim')
