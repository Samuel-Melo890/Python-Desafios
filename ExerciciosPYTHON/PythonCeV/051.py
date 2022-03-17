print('='*8,'Progressao Aritmetica','='*8)

pt = int(input('Diga o primeiro termo da sua PA: '))
r = int(input('Diga a razao da sua PA: '))
dt = pt + (10 - 1)*r
for n in range(pt, dt + 1, r):
    print(n, end = '->')
print('FIM')
