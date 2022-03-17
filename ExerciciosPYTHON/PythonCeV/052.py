print('='*8,'Números Primos','='*8)

cont = 0
n = int(input('Digite um número inteiro qualquer: '))
print(f'O número {n} é divisível por:')
for p in range(1 , n + 1):
    if n % p == 0:
        print(f'\033[4;32m{p}\033[m', end = ' ')
        cont = cont + 1
if cont == 2:
    print(f'\nO número {n} é um número \033[36mPRIMO\033[m!')
else:
    print(f'\nO número {n} \033[31mNÃO\033[m é um número \033[36mPRIMO\033[m!')
