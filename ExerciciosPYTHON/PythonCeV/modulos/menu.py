def linha(n=1):
    print('-' * n)


def titulo(s):
    linha(40)
    print(s.center(40))
    linha(40)


def menu(list):
    titulo('Menu Principal')
    for p, v in enumerate(list):
        print(f'\033[36m{p + 1}\033[m: \033[32m{v}\033[m')
