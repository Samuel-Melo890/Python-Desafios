print('='*8,'Simulador de Caixa Eletrônico','='*8)
print('-=-'*12)
print('{:^36}'.format('Banco Jailson Mendes'))
print('-=-'*12)
v = int(input('Qual será o valor a ser sacado? R$'))
c50 = c20 = c10 = c1 = 0
while True:
    while v >= 50:
        v -= 50
        c50 += 1
    while v >= 20:
        v -= 20
        c20 += 1
    while v >= 10:
        v -= 10
        c10 += 1
    while v >= 1:
        v -= 1
        c1 += 1
    if v == 0:
        break
print('O valor a ser sacado deverá ser entregue em:')
if c50 != 0:
    print(f'{c50} cédulas de R$50')
if c20 != 0:
    print(f'{c20} cédulas de R$20')
if c10 != 0:
    print(f'{c10} cédulas de R$10')
if c1 != 0:
    print(f'{c1} cédulas de R$1.')
