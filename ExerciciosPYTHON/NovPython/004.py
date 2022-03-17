print('='*8,'Par ou Ímpar','='*8)
from module import calculadora, interface
from time import sleep

while True:
    interface.menu('Par ou Ímpar?')
    try:
        j1 = int(input('Jogador 1 => Escolha um número inteiro positivo qualquer: '))
        j1_s = ' '
        while j1_s not in "PIÍ":
            j1_s = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
        j2 = int(input('Jogador 2 => Escolha um número inteiro positivo qualquer: '))
    except (ValueError, TypeError):
        print('\033[31mValor dado inválido! Por favor digite um número inteiro positivo!\033[m')
    except KeyboardInterrupt:
        print('\033[36mValor não fornecido! Tente de novo\033[m')
    except IndexError:
        print('\033[31mERRO! Por favor escolha entre P ou I!\033[m')
    else:
        print(f'{j1} + {j2} = {calculadora.som(j1, j2)}')
        sleep(1.5)
        if j1_s in 'P':
            if calculadora.som(j1, j2) % 2 == 0:
                print('\033[35mDeu Par!\033[m')
                print('\033[32mJogador 1 venceu! Parabéns!\033[m')
            else:
                print('\033[35mDeu Ímpar!\033[m')
                print('\033[32mJogador 2 venceu! Parabéns!\033[m')
        else:
            if calculadora.som(j1, j2) % 2 == 0:
                print('\033[35mDeu Par!\033[m')
                print('\033[32mJogador 2 venceu! Parabéns!\033[m')
            else:
                print('\033[35mDeu Ímpar!\033[m')
                print('\033[32mJogador 1 venceu! Parabéns!\033[m')
        sleep(1)
        r = ' '
        while r not in 'SN':
            r = str(input('Quer jogar de novo? [S/N] ')).strip().upper()[0]
        if r in 'N':
            break
print('\033[36mPrograma Finalizado!\033[m')
