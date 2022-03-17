print('='*8,'Primeiro e Ultimo Nome de uma Pessoa','='*8)

n = str(input('Qual o seu nome completo?')).strip().title()
nsep = n.split()
print('''O seu primeiro nome e {}.
O seu ultimo nome e {}.'''.format(nsep[0],nsep[-1]))
