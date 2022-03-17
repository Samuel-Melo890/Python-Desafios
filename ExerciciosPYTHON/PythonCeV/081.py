print('='*8,'Extraindo Dados de Uma Lista','='*8)
l = []
while True:
    l.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar a digitar valores? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Sua lista ficou: {l}')
print(f'Você digitou {len(l)} números.')
if 5 in l:
    print(f'O valor 5 se encontra na lista!')
else:
    print('O valor 5 não se encontra na lista.')
l.sort(reverse = True)
print(f'Sua lista em ordem descrescente fica: {l}')
