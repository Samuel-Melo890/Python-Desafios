def aumentar(p=0, t=0, c=False):
    t = t / 100
    res = p * (1 + t)
    if c:
        return moeda(res)
    else:
        return res


def diminuir(p=0, t=0, c=False):
    t = t / 100
    res = p * (1 - t)
    if c:
        return moeda(res)
    else:
        return res


def dobro(p=0, c=False):
    res = p * 2
    if c:
        return moeda(res)
    else:
        return res

def metade(p=0, c=False):
    res = p / 2
    if c:
        return moeda(res)
    else:
        return res


def moeda(p=0):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p=0, ta=0, tr=0):
    print('-' * 40)
    print(f'{"Resumo do Valor":^40}')
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do Preço: \t{dobro(p, True)}')
    print(f'Metade do Preço: \t{metade(p, True)}')
    print(f'Aumento de {ta}%: \t{aumentar(p, ta, c=True)}')
    print(f'Redução de {tr}%: \t{diminuir(p, tr, c=True)}')
    print('-' * 40)
