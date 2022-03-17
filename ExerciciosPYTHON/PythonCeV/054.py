print('='*8,'Grupo da Maioridade','='*8)

from datetime import date
menor = 0
maior = 0
for p in range(1, 8):
    dt = int(input('Data de nascimento da pessoa número {}: '.format(p)))
    idade = date.today().year - dt
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Existem {} pessoas menores de idade e {} pessoas maiores de idade.'.format(menor, maior))
