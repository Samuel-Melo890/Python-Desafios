print('='*8,'Validação de Dados','='*8)

sex = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Dados inválidos! Por favor informe seu sexo corretamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sex))
