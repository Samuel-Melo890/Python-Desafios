print('='*8,'Unindo Dicionários e Listas','='*8)
l = []
d = {}
s = m = 0
while True:
    d['nome'] = str(input('Nome: ')).strip().title()
    d['sexo'] = ' '
    while d['sexo'] not in 'MF':
        d['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    d['idade'] = int(input('Idade: '))
    s += d['idade']
    l.append(d.copy())
    d.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
m = s / len(l)
print(f'Foram cadastradas um total de {len(l)} pessoas.')
print(f'A média de idade do grupo é de {m:.2f} anos.')
lm = []
liam = []
dam = {}
for p in l:
    if p['sexo'] in 'F':
        lm.append(p['nome'])
    if p['idade'] > m:
        dam['nome'] = p['nome']
        dam['idade'] = p['idade']
        liam.append(dam.copy())
        dam.clear()
print(f'As mulheres cadastradas foram: {lm}')
print('As pessoas com idade acima da média foram:')
for p in liam:
    print(f'    -{p["nome"]} com {p["idade"]} anos.')
