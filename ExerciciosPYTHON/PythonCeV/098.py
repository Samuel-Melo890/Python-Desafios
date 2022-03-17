print('='*8,'Função de Contador','='*8)
def contador(i, f, p):
    from time import sleep
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} pulando de {p} em {p}:')
    if i > f:
        p = -p
        for c in range(i, f - 1, p):
            print(f'\033[32m{c}\033[m', end = '  ', flush = True)
            sleep(0.5)
            if c == f:
                print()
    else:
        for c in range(i, f + 1, p):
            print(f'\033[32m{c}\033[m', end = '  ', flush = True)
            sleep(0.5)
            if c == f:
                print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize sua contagem!')
começo = int(input('Ínicio: '))
final = int(input('Fim: '))
passo = int(input('Passo: '))
contador(começo, final, passo)
