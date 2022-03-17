print('='*8,'Ficha do Jogador','='*8)
def ficha(n='<Desconhecido>',g=0):
    """Fornece a ficha técnica de um jogador

    Args:
        n (str, optional): Nome do jogador. Defaults to '<Desconhecido>'.
        g (int, optional): Número de gols marcados. Defaults to 0.
    """
    print('-=' * (len(n) + 20))
    print(f'O jogador \033[36m{n}\033[m fez \033[32m{g}\033[m gols no campeonato.')
    print('-=' * (len(n) + 20))


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Gols no campeonato: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(g=g)
else:
    ficha(n, g)
