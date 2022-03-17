print('='*8,'Dicionário Em Python','='*8)
d = {}
d['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
d['média'] = float(input(f'Digite a média de {d["nome"]}: '))
if d['média'] <= 5:
    d['situação'] = 'Reprovado!'
elif 5 < d['média'] < 7:
    d['situação'] = 'Recuperação!'
else:
    d['situação'] = 'Aprovado!'
for k, v in d.items():
    print(f'{k.title()}: {v}')
