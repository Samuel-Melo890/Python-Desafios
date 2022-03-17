print('='*8,'Funções para Votação','='*8)
def voto(nasc):
    """Informa se a pessoa pode ou nao votar.

    Args:
        nasc (int): Ano de nascimento da pessoa.

    Returns:
        Idade da pessoa e se seu voto é negado, opcional ou obrigatório.
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos o voto é \033[31mNegado\033[m.'
    elif 16 <= idade < 18 or idade >= 60:
        return f'Com {idade} anos o voto é \033[33mOpcional\033[m.'
    else:
        return f'Com {idade} anos o voto é \033[36mObrigatório\033[m.'


nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
