print('='*8,'Alistamento Militar','='*8)

sex = str(input('Qual o seu sexo? Responda com M/F: ')).strip().upper()
if sex == 'F':
    print('Voce nao precisa fazer o alistamento militar.')
elif sex == 'M':
    from datetime import date
    an = int(input('Qual o seu ano de nascimento? '))
    aat = date.today().year
    idade = aat - an
    print('Quem nasceu em {} tem {} anos em {}.'.format(an,idade,aat))
    if idade < 18:
        print('Esta pessoa ainda nao pode fazer o alistamento militar. Devera esperar mais {} ano(s).'.format(18 - idade))
        dta = aat + (18 - idade)
        print('Seu alistamento sera em {}.'.format(dta))
    elif idade > 18:
        print('Essa pessoa ja passou do tempo de seu alistamento em {} ano(s).'.format(idade - 18))
        dta = aat - (idade - 18)
        print('Seu alistamento deveria ter sido em {}.'.format(dta))
    else:
        print('Essa pessoa devera se alistar ainda esse ano.')
else:
    print('{}Opcao invalida!{}'.format('\033[31m','\033[m'))
