print('='*8,'Entrada de dados Monetários','='*8)
from modulos import moeda
from modulos import dado
p = dado.leiaDinheiro('Digite um preço: R$')
print(f'O dobro de {moeda.moeda(p)} é de {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é de {moeda.metade(p, True)}')
print(f'Com um aumento de 65%, temos {moeda.aumentar(p, 65, c=True)}')
