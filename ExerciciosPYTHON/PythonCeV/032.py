print('='*8,'Ano Bissexto','='*8)

from datetime import date
a = int(input('Digite o ano que quer analisar, caso queira analisar o ano atual digite 0: '))
if a==0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} {}e um ano bissexto{}.'.format(a,'\033[4;36m','\033[m'))
else:
    print('O ano de {} {}nao e bissexto{}.'.format(a,'\033[4;31m','\033[m'))
