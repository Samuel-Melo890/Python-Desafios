print('='*8,'Funções Aprofundadas em Python','='*8)
def leiaInt(s):
    while True:
        try:
            n = int(input(s))
        except (ValueError, TypeError):
            print('\033[31mValor dado inválido! Tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\nO usuário interrompeu a entrada de dados')
            return 0
        else:
            return n


def leiaFloat(s):
    while True:
        try:
            n = float(input(s))
        except (ValueError, TypeError):
            print('\033[31mValor dado inválido! Tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\nO usuário interrompeu a entrada de dados')
            return 0
        else:
            return n


n = leiaInt('Digite um número Inteiro: ')
print(f'O número digitado foi {n}.')

f = leiaFloat('Digite um número Real: ')
print(f'O número digitado foi {f}.')
