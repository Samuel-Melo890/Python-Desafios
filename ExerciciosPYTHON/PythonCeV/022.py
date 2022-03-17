print('='*8,'Analisador de Textos','='*8)
nome = input('Digite seu nome completo:').strip()
nma = nome.upper()
nmi = nome.lower()
sep = nome.split()
ql = len(''.join(sep))
ql1 = len(sep[0])
print('''Analisando seu texto...
O seu nome todo em maiusculo e : {}
O seu nome todo em minusculo e : {}
Seu nome completo tem {} letras.
Seu primeiro nome tem {} letras.'''.format(nma,nmi,ql,ql1))
