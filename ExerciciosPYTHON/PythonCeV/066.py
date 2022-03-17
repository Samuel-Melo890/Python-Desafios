print('='*8,'Vários Números com Flag','='*8)
qn = s = 0
while True:
    n = int(input('Digite um número inteiro [digite 999 caso queira parar]: '))
    if n == 999:
        break
    qn = qn + 1
    s = s + n
print(f'Você digitou \033[4;36m{qn}\033[m números e a soma entre eles vale \033[4;36m{s}\033[m.')
