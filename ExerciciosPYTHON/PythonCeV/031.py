print('='*8,'Custo da Viagem','='*8)

d = float(input('De quantos km se trata a viagem? '))
if d>200:
    v2 = 0.45*d
    print('O custo da viagem devera ser de R${}.'.format(v2))
else:
    v1 = 0.5*d
    print('O custo da viagem devera ser de R${}.'.format(v1))

