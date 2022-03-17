print('='*8,'Progressão Aritmética v2.0','='*8)

pt = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
t = pt
c = 1
print('Sua progressão aritmética fica:')
while c <= 10:
    print(t, end = ' => ')
    t = t + r
    c += 1
print('Fim')
