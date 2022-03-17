print('='*8,'Funções Para Sortear e Somar','='*8)
núm = []
def sorteio(lst):
    from random import randint
    from time import sleep
    while True:
        n = randint(0, 10)
        if n not in lst:
            lst.append(n)
        if len(lst) == 5:
            break
    print(f'Os números sorteados para a lista foram:', end = ' ')
    for n in lst:
        print(f'\033[32m{n}\033[m', end = ' ', flush = True)
        sleep(1)
        if n == lst[-1]:
            print()
def somaPar(lst):
    lp = []
    for p in lst:
        if p % 2 == 0:
            lp.append(p)
    print(f'Os números pares presentes na lista {lst} foram {lp} e a soma entre eles vale {sum(lp)}.')


sorteio(núm)
somaPar(núm)
