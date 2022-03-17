print('='*8,'Matriz em Python','='*8)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l  in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()

'''l = [[], [], []]
cont = cont1 = cont2 = 0
for c in range(0, 9):
    if c < 3:
        n = int(input(f'Digite um valor para a posição [0, {cont}]: '))
        l[0].append(n)
        cont += 1
    elif c < 6:
        n = int(input(f'Digite um valor para a posição [1, {cont1}]: '))
        l[1].append(n)
        cont1 += 1
    else:
        n = int(input(f'Digite um valor para a posição [2, {cont2}]: '))
        l[2].append(n)
        cont2 += 1
print('Sua matriz ficará dessa forma:')
print(f'[ {l[0][0]} ] [ {l[0][1]} ] [ {l[0][2]} ]')
print(f'[ {l[1][0]} ] [ {l[1][1]} ] [ {l[1][2]} ]')
print(f'[ {l[2][0]} ] [ {l[2][1]} ] [ {l[2][2]} ]')'''
