print('='*8,'Formatando Moedas em Python','='*8)
from modulos import moeda
p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 25%, temos {moeda.moeda(moeda.aumentar(p, 25))}')
print(f'Reduzindo 10%, temos {moeda.moeda(moeda.diminuir(p, 10))}')
