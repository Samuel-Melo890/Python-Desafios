print('='*8,'Análise de Dados em Uma Tupla','='*8)
t = (int(input('Digite o seu primeiro valor: ')),
    int(input('Digite o seu segundo valor: ')),
    int(input('Digite o seu terceiro valor: ')),
    int(input('Digite o seu quarto valor: ')))
print('Os valores digitados foram:')
for n in t:
    print(n, end = ' ')
print(f'\nO valor 9 apareceu \033[32m{t.count(9)} vezes\033[m.')
if 3 in t:
    print(f'O valor 3 foi digitado primeiramente na \033[32mposição {(t.index(3)) + 1}\033[m.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram:', end = ' ')
cont = 0
for p in t:
    if p % 2 == 0:
        cont += 1
        print(f'\033[32m{p}\033[m', end = ' ')
if cont == 0:
    print('\033[31mNenhum valor par digitado\033[m.')
