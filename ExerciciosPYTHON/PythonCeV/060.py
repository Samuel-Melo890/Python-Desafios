print('='*8,'Cálculo do Fatorial','='*8)

n = int(input('Digite um número inteiro qualquer: '))
fat = 1
print('O fatorial de {} vale:'.format(n))
while n != 0:
    if n != 0:
        print(n, end = '')
        if n > 1:
            print(' x ', end = '')
        else:
            print(' = ', end = '')
    if n != 0:
        fat *= n
    n = n - 1
print('{}'.format(fat))

'''for n in range(n, 0, -1):
    print(n, end = ' ')
    if n > 1:
        print('x ', end = '')
    else:
        print('= ', end = '')
    fat *= n
print(fat)'''
