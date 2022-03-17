print('='*8,'Super Progressão Aritmética v3.0','='*8)

pt = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
t = pt
qt = 0
op = 10
print('Sua progressão aritmética fica:')
while op != 0:
    print(t, end = ' => ')
    t += r
    qt += 1
    op -= 1
    if op == 0:
        print('Pausa')
        op = int(input('Quantos termos quer mostrar a mais? '))
print('A progressão foi finalizada com {} termos mostrados.'.format(qt))
