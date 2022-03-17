print('='*8,'Validando Entrada de Dados em Python','='*8)
def leiaInt(s):
    """Lê uma string e recebe um valor inteiro.

    Args:
        s (str): A frase que será escrita.

    Returns:
        O valor númerico inteiro digitado pelo usuário.
    """
    while True:
        n = input(s)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(f'\033[1;31mErro! Digite um número inteiro!\033[m')
    return n


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
