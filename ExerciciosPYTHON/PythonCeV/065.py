print('='*8,'Maior e Menor Valores','='*8)

r = 'S'
qv = s = m = 0
maior = menor = 0
while r in 'S':
    n = int(input('Digite um número inteiro: '))
    qv = qv + 1
    s = s + n
    if qv == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar a digitar valores?[S/N] ')).strip().upper()[0]
m = s / qv
print('A média entre os valores digitados vale {}. O menor valor foi {} e o maior foi {}.'.format(m, menor, maior))
