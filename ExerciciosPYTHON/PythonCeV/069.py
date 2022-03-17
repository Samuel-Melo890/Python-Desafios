print('='*8,'Análise de Dados do Grupo','='*8)
cida = chom = cmul = 0
while True:
    print('\033[34m=-==-= Cadastro de Uma Pessoa =-==-=\033[m')
    sex = str(input('Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Digite CORRETAMENTE o sexo da pessoa: [M/F] ')).strip().upper()[0]
    if sex in 'M':
        chom += 1
    idade = int(input('Digite a idade da pessoa: '))
    if idade > 18:
        cida += 1
    if idade < 20:
        if sex in 'F':
            cmul += 1
    print('\033[34m=-=\033[m' * 12)
    p = str(input('Quer continuar a cadastrar pessoas? [S/N] ')).strip().upper()[0]
    while p not in 'NS':
        p = str(input('Quer continuar a cadastrar pessoas? [S/N] ')).strip().upper()[0]
    if p in 'N':
        break
print('\033[36m=-=Fim do Cadastro=-=\033[m')
print(f'>>Você registrou {cida} pessoa(s) com mais de 18 anos.')
print(f'>>Você registrou cerca de {chom} homem(ns).')
print(f'>>Você registrou cerca de {cmul} mulher(es) com menos de 20 anos.')
