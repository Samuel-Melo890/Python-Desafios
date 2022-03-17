from os import system

system('cls')

print('='*8,'Multiplicação Lambda','='*8)

mult = lambda a=1, b=1: a * b

while True:
    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    except (ValueError, TypeError):
        print('\033[31mERRO! Por favor digite um número inteiro!\033[m')
    else:
        print(f'O resultado da multiplicação entre \033[4m{n1}\033[m e \033[4m{n2}\033[m é \033[4;35m{mult(n1, n2)}\033[m!')
        break
