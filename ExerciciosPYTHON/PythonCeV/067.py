print('='*8,'Tabuada v3.0','='*8)
print('Digite os números que quiser para ver suas respectivas tabuadas!!! \nCaso queira parar o programa digite um número negativo.')
while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        break
    tab = 1
    print('\033[34m-=\033[m' * 12)
    while tab < 11:
        print(f'{n} X {tab} = {n * tab}')
        tab = tab + 1
    print('\033[34m-=\033[m' * 12)
print('\033[36mPrograma finalizado!\033[m')
