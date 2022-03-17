print('='*8,'Aprimorando os Dicionários','='*8)
lj = []
jog = {}
while True:
    jog['nome'] = str(input('Nome do jogador: ')).strip().title()
    qp = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    gols = []
    for c in range(0, qp):
        gols.append(int(input(f'    Número de gols na partida {c + 1}: ')))
    jog['gols'] = gols[:]
    tot = 0
    tot = sum(gols)
    jog['total'] = tot
    lj.append(jog.copy())
    tot = 0
    gols.clear()
    jog.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 45)
print(f'{"Cód.":<3} {"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-' * 40)
for cod, j in enumerate(lj):
    print(f'{cod:>3} ', end = ' ')
    for v in j.values():
        print(f'{str(v):<15}', end = '')
    print()
print('-' * 40)
while True:
    d = int(input('Quer ver os dados de qual jogador? [Digite 999 para parar] '))
    if d == 999:
        break
    elif d < 0 or d >= len(lj):
            print('\033[31mCódigo do jogador não encontrado!\033[m\nTente novamente:')
    else:
        print(f'Levantamento do jogador {lj[d]["nome"]}:')
        for p, g in enumerate(lj[d]["gols"]):
            print(f'    Na partida {p + 1}: {lj[d]["nome"]} fez {g} gols.')
print('\033[36mPrograma finalizado!\033[m')
