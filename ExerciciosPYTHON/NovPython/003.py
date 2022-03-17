print('='*8,'Calculadora','='*8)
from module import interface
from module import calculadora
from time import sleep

while True:
    interface.menu('Calculadora')
    op = interface.options('Somar', 'Subtrair', 'Dividir', 'Multiplicar', 'Sair do Programa')
    if 1 <= op <= 4:
        while True:
            try:
                sleep(0.5)
                n1 = int(input('Digite o primeiro valor: '))
                n2 = int(input('Digite o segundo valor: '))
            except (ValueError, TypeError):
                print('\033[31mValores dados não válidos! Por favor digite um número inteiro!\033[m')
            except KeyboardInterrupt:
                print('\033[36mValor não fornecido! Por favor digite um valor inteiro\033[m')
            else:
                if op == 1:
                    interface.titulo('Soma')
                    print(f'{n1} + {n2} = {calculadora.som(n1, n2)}')
                    sleep(1)
                    break
                elif op == 2:
                    interface.titulo('Subtração')
                    print(f'{n1} - {n2} = {calculadora.sub(n1, n2)}')
                    sleep(1)
                    break
                elif op == 3:
                    interface.titulo('Divisão')
                    print(f'{n1} : {n2} = {calculadora.div(n1, n2)}')
                    sleep(1)
                    break
                elif op == 4:
                    interface.titulo('Multiplicação')
                    print(f'{n1} x {n2} = {calculadora.mult(n1, n2)}')
                    sleep(1)
                    break
    else:
        interface.titulo('Saindo do Programa...')
        sleep(2)
        break
print('\033[36mPrograma Finalizado!\033[m')
