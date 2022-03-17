print('='*8,'Mais Sobre Matriz em Python','='*8)
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc3 = mai2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if m[l][c] % 2 == 0:
            sp += m[l][c]
        sc3 += m[l][2]
        if c == 0:
            mai2 = m[1][c]
        else:
            if m[1][c] > mai2:
                mai2 = m[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end = '')
    print()
print(f'A soma de todos os valores pares é de {sp}.')
print(f'A soma dos valores da terceira coluna é {sc3}.')
print(f'O maior valor da segunda linha foi o {mai2}.')
