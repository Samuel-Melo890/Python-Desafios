print('='*8,'Verificando as Primeiras Letras de um Texto','='*8)
c = input('Qual o nome da sua cidade?').strip()
l = c.upper().split()
print('O nome da cidade comeca com a palavra Santo? {}'.format(l[0]=='SANTO'))
