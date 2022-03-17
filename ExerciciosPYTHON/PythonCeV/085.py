print('='*8,'Listas com Pares e Ímpares','='*8)
l = [[], []]
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        l[0].append(n)
        l[0].sort()
    else:
        l[1].append(n)
        l[1].sort()
print(f'Sua lista de valores separados em par/ímpar e em ordem crescente fica: \n{l[0]}\n{l[1]}')
