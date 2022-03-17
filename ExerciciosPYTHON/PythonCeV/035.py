print('='*8,'Analisador de Triangulos','='*8)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
#l = [s1,s2,s3]
#mav = max(l)
#if (s1 + s2 + s3) - mav > mav:
    #print('Esses segmentos {}podem{} formar um triangulo!'.format('\033[4;32m','\033[m'))
#else:
    #print('Esse segmentos {}nao podem{} formar um triangulo!'.format('\033[4;31m','\033[m'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Esses segmentos {}podem{} formar um triangulo!'.format('\033[4;32m','\033[m'))
else:
    print('Esses segmentos {}nao podem{} formar um triangulo!'.format('\033[4;31m','\033[m'))
