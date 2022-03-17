print('='*8,'Seno, Cosseno e Tangente','='*8)
a = float(input('Digite o seu angulo:'))
from math import radians, sin, cos, tan
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('''Para o angulo analisado {}, temos:
Seno igual a {:.2f}
Cosseno igual a {:.2f}
Tangente igual a {:.2f}'''.format(a,s,c,t))
