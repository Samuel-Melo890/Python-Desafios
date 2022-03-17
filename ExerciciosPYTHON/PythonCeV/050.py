print('='*8,'Soma dos Pares','='*8)

s = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite o {} valor inteiro: '.format(n)))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print('A somatoria dos {} valores {}PARES{} dados foi de {}.'.format(cont,'\033[36m','\033[m',s))
