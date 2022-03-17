print('='*8,'Lista Composta e Análise de Dados','='*8)
pp = []
dados = []
mai = men = 0
while True:
    n = (str(input('Nome: ')).strip().title())
    p = (float(input('Peso: ')))
    dados.append(n)
    dados.append(p)
    if len(pp) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pp.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar a cadastrar pessoas? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Foram cadastradas um total de {len(pp)} pessoas.')
print(f'O maior peso registrado foi de {mai:.1f}kg das pessoas: ', end = '')
for pes in pp:
    if pes[1] == mai:
        print(f'[{pes[0]}]', end = ' ')
print(f'\nO menor peso registrado foi de {men:.1f}kg das pessoas: ', end = '')
for pes in pp:
    if pes[1] == men:
        print(f'[{pes[0]}]', end = ' ')
