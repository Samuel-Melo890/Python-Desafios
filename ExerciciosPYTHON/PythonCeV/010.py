print('='*8,'Conversao de Real para Dolar','='*8)
r = float(input('Quanto dinheiro voce tem em sua carteira? R$'))
us = r/3.27
print('Com R${:.2f} voce pode comprar cerca de US${:.2f}!'.format(r,us))
