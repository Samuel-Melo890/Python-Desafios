print('='*8,'Valores Únicos em Uma Lista','='*8)
v = []
print('Vamos fazer uma lista de números!')
while True:
    n = int(input('Digite um valor: '))
    if n in v:
        print('\033[33mValor repetido! Não será adicionado!\033[m')
    if n not in v:
        v.append(n)
        print('\033[32mValor novo adicionado!\033[m')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar a adicionar números? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Sua lista fica: {v}')
v.sort()
print(f'A lista dos valores digitados em ordem crescente fica: {v}')
