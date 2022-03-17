print('='*8,'Lista de Preços com Tupla','='*8)
pp = ('Lapiseira', 5, 'Computador', 2150, 'Mochila', 120, 'Mouse', 50, 'Mousepad', 60, 'Caderno', 100, 'Livro', 35, 'Bolacha', 8, 'Cadeira Gamer', 1500, 'Boné', 15)
print('-' * 46)
print(f'{"Listagem de Preços":^46}')
print('-' * 46)
print('-=' * 23)
for pos in range(0, len(pp)):
    if pos % 2 == 0:
        print(f'{pp[pos]:.<35}', end = '')
    elif pos % 2 == 1:
        print(f'R${pp[pos]:>8.2f}')
print('-=' * 23)
