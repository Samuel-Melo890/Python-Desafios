print('='*8,'Função para Fatorial','='*8)
def fatorial(n, show=False):
    """Calcula o fatorial de um número.

    Args:
        n (int): O número a ter seu fatorial calculado.
        show (bool, optional): Mostrar ou nao a conta. Defaults to False.

    Returns:
        O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
    return f


n = int(input('Digite um número para ver seu fatorial: '))
while True:
    r = str(input('Deseja ver o cálculo do fatorial? [S/N] ')).strip().upper()[0]
    if r in 'SN':
        break
if r in 'S':
    show = True
else:
    show = False

print(f'O fatorial de {n} é :')
print(fatorial(n, show))
