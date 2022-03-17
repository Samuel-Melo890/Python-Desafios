from os import system

system('cls')

print('='*8,'Filtro de Números','='*8)

numeros = []
cont = 0

while True:
    try:
        num = int(input('Digite um número: '))
    except (ValueError, TypeError, KeyboardInterrupt):
        print('\033[31mERRO! Por favor insira um número inteiro!\033[m')
        continue
    else:
        cont += 1
        numeros.append(num)
        if cont == 5:
            break

maior_10 = filter(lambda valor: valor >= 10, numeros)

print('Os números digitados que foram maiores ou iguais a 10 foram:')
for n in maior_10:
    print(n)
