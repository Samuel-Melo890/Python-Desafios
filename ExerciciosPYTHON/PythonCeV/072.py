print('='*8,'Número Por Extenso','='*8)
c = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'O número \033[4;32m{n}\033[m por extenso fica \033[36m{c[n]}\033[m!')
        r = ' '
        while r not in 'SN':
            r = str(input('Quer continuar a ver os números por extenso? [S/N] ')).strip().upper()[0]
        if r in 'N':
            break
print('\033[36mPrograma finalizado!\033[m')
