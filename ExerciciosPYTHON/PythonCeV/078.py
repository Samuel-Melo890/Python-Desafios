print('='*8,'Maior e Menor Valores na Lista','='*8)
v = []
mai = men = 0
for n in range(0, 5):
    v.append(int(input(f'Digite um valor para a Posição {n}: ')))
    if n == 0:
        mai = men = v[n]
    else:
        if v[n] > mai:
            mai = v[n]
        if v[n] < men:
            men = v[n]
print(f'Sua lista ficou: {v}')
print(f'O maior valor foi o número {mai} nas posições ', end = '')
for p, valor in enumerate(v):
    if valor == mai:
        print(f'{p}...', end = ' ')
print(f'\nO menor valor foi o número {men} nas posições ', end = '')
for p, valor in enumerate(v):
    if valor == men:
        print(f'{p}...', end = ' ')
