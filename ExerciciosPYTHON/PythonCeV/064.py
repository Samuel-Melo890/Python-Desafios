print('='*8,'Tratando Vários Valores v1.0','='*8)

n = qn = s = 0
while n != 999:
    n = int(input('Digite um número inteiro qualquer [999 é a condição de parada]: '))
    if n != 999:
        qn += 1
        s += n
print('Você digitou {} números e o valor da soma entre eles foi de {}.'.format(qn, s))
