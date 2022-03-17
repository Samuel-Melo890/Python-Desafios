print('='*8,'Lista Ordenada Sem Repetições','='*8)
l = []
for c in range(0, 5):
    n = int(input('Digite um valor para a lista: '))
    if c == 0:
        l.append(n)
    elif n > l[-1]:
        l.append(n)
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                break
            pos += 1
print(f'Sua lista em ordem crescente fica: {l}')
