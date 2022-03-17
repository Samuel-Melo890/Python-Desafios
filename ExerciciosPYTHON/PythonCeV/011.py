print('='*8,'Tinta para Pintar Parede','='*8)
l = float(input('Qual a largura da parede em metros?'))
a = float(input('Qual a altura da parede em metros?'))
a2 = a*l
qt = a2/2
print('''As dimensoes dessa parede sao de {}x{}.
A area desta parede equivale a {} metros quadrados.
Para pinta-la serao necessarios cerca de {} litros de tinta.'''.format(l,a,a2,qt))
