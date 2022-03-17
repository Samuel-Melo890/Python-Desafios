print('='*8,'Separando Digitos de um Numero','='*8)

n = int(input('Digite um numero entre 0 e 9999:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 
print('Analisando o numero {}...'.format(n))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u,d,c,m))
