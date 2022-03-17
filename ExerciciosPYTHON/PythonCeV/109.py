print('='*8,'Formatando Ainda Mais Moedas em Python','='*8)
from modulos import moeda
p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, c=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, c=True)}')
print(f'Aumentando 20%, temos {moeda.aumentar(p, 20, c=True)}')
print(f'Reduzindo 15%, temos {moeda.diminuir(p, 15, c=True)}')
