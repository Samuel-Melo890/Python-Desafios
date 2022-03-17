print('='*8,'Cadastro de Jogador de Futebol','='*8)
jogador = {}
jogador['nome'] = str(input('Nome: ')).strip().title()
qp = int(input('Quantas partidas já participou: '))
gols = []
for c in range(0, qp):
    gols.append(int(input(f'    Quantos gols fez na partida {c + 1}? ')))
jogador['gols'] = gols[:]
totgol = sum(gols)
jogador['total'] = totgol
print('-=' * 25)
print(jogador)
print('-=' * 25)
for k, v in jogador.items():
    print(f'{k.title()} é {v}')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {qp} partidas.')
for p, v in enumerate(jogador['gols']):
    print(f'    => Na partida {p + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
