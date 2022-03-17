print('='*8,'Soma de Impares Multiplos de Tres','='*8)

s = 0
cont = 0
for n in range(3, 501, 6):
    print(n)
    #s += n
    s = s + n
    cont = cont + 1
print('A somatoria dos numeros foi de {} e o total de valores foi de {}.'.format(s,cont))
