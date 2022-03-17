def menu(s):
    print('-' * 40)
    print(f'{s.center(40)}')
    print('-' * 40)


def options(* str):
    for n, i in enumerate(str):
        print(f'\033[32m{n + 1}\033[m: {i.title()}')
    while True:
        try:
            op = int(input('Qual sua escolha? '))
        except (ValueError, TypeError):
            print('\033[31mValor dado inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[36mUsuário não forneceu os dados!\033[m')
        else:
            if op > len(str) or op < 1:
                print('\033[31mOpção inválida!\033[m')
            else:
                return op

def titulo(str):
    print('-' * 25)
    print(f'{str.center(25)}')
    print('-' * 25)