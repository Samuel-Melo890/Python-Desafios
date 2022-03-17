print('='*8,'Tabuada v2.0','='*8)

n = int(input('Digite um numero inteiro qualquer: '))
print('A tabuada do numero {} e a seguinte:'.format(n))
print('-='*8)
for t in range(1, 11):
    print('{} X {} = {}'.format(n,t,n*t))
print('-='*8)
