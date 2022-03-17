print('='*8,'Estatísticas em Produtos','='*8)
sp = m1000 = 0
cont = 0
nombar = ''
prebar = 0
while True:
    n = str(input('Qual o nome do produto? ')).strip().title()
    p = float(input('Qual o preço do produto? R$'))
    sp += p
    if p > 1000:
        m1000 += 1
    cont += 1
    if cont == 1:
        prebar = p
        nombar = n
    else:
        if p < prebar:
            prebar = p
            nombar = n
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar a cadastrar produtos? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('\033[36m<<Cadastro finalizado!>>\033[m')
print(f'>>Você gastou um total de R${sp:.2f} em suas compras.')
print(f'>>Você comprou {m1000} produto(s) que custam mais que R$1000.')
print(f'>>O produto mais barato que você comprou foi o {nombar} custando R${prebar:.2f}.')
