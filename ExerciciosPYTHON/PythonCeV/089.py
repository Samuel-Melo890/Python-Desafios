print('='*8,'Boletim Com Listas Compostas','='*8)
l = []
dados = []
while True:
    dados.append(str(input('Nome do aluno: ')).strip().title())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    l.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer cadastrar mais alunos? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(f'{"-=" * 20}')
print(f'{"No.":<4} {"Nome":<15}  {"Média"}')
for o, a in enumerate(l):
    m = (a[1] + a[2]) / 2
    print(f'{o:<4} {a[0]:-<15}>{m:>6.1f}')
print(f'{"-=" * 20}')
while True:
    p = int(input('Quer ver as notas de qual aluno? [Digite 999 para parar] '))
    if p == 999:
        break
    for o, a in enumerate(l):
        if p == o:
            print(f'Notas do aluno {a[0]}:\nNota 1: {a[1]}\nNota 2: {a[2]}')
print('\033[36mPrograma finalizado!\033[m')
