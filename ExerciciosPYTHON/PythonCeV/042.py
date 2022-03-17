print('='*8,'Analisando Triangulos v2.0','='*8)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Esses segmentos podem formar um triangulo ', end='')
    if s1 == s2 == s3:
        print('EQUILATERO!')
    elif s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print('ISOSCELES!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
else:
    print('Esses segmentos nao podem formar um triangulo!')
