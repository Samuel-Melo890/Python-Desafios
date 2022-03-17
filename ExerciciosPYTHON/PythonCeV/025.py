print('='*8,'Procurando uma String Dentro de Outra','='*8)

n = input('Qual o seu nome completo?').strip().lower()
if 'silva' in n:
    print('O seu nome possui a palavra Silva nele.')
else:
    print('O seu nome nao possui a palavra Silva nele.')
    