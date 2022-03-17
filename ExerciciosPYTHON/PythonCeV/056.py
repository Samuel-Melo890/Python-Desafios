print('='*8,'Analisador Completo','='*8)

m = 0
ihmv = 0
hmv = ''
cont = 0
for p in range(1 , 5):
    print('---- Pessoa Número {} ----'.format(p))
    n = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    m += idade / 4
    if sex == 'M':
        if p == 1:
            ihmv = idade
            hmv = n
        else:
            if idade > ihmv:
                ihmv = idade
                hmv = n
    if sex == 'F':
        if idade < 20:
            cont += 1
print('A média de idade deste grupo é de {:.2f} anos.'.format(m))
print('O nome do homem mais velho é {} com {} anos.'.format(hmv, ihmv))
print('Existe um total de {} mulher(es) com menos de 20 anos.'.format(cont))
