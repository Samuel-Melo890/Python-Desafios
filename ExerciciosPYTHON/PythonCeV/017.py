print('='*8,'Calculo da Hipotenusa','='*8)
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
from math import hypot
h = hypot(co,ca)
#h = (ca**2 + co**2)**(1/2)
print('A hipotenusa desse triangulo retangulo vale {:.2f}.'.format(h))
