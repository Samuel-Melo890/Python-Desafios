print('='*8,'Função que Descobre O Maior','='*8)
def maior(* n):
    from time import sleep
    print('Analisando números...')
    sleep(2)
    for num in n:
        print(f'\033[36m{num}\033[m', end = '  ', flush = True)
        sleep(0.5)
    print(f'\nForam passados {len(n)} valores e o maior deles foi o ', end = '')
    if len(n) == 0:
        print(0)
    else:
        print(f'\033[34m{max(n)}\033[m')


maior(1, 5, 7, 2, 9, 8, 4)
