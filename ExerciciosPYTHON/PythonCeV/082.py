print('='*8,'Dividindo Valores em Várias Listas','='*8)
l = []
lp = []
li = []
while True:
    l.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar a dar valores? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
for num in l:
    if num % 2 == 0:
        lp.append(num)
    else:
        li.append(num)
print(f'A sua lista completa ficou: {l}')
print(f'A sua lista apenas com os valores pares fica: {lp}')
print(f'A sua lista apenas com os valores ímpares fica: {li}')
