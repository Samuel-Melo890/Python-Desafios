print('='*8,'Detector de Palíndromo','='*8)

f = str(input('Digite uma frase: ')).strip().upper().split()
fj = ''.join(f)
r = fj[::-1]
print('A frase {}{}{} de trás para frente fica {}{}{}.'.format('\033[4m', fj, '\033[m', '\033[4m', r, '\033[m'))
if fj == r:
    print('Portanto essa frase é um {}PALÍNDROMO{}!'.format('\033[36m' , '\033[m'))
else:
    print('Portanto essa frase {}NÃO{} é um {}PALÍNDROMO{}!'.format('\033[31m' , '\033[m' , '\033[36m' , '\033[m'))
#r = ''
#for l in range(len(fj) -1, -1, -1):
    #r += fj[l]
#print('O inverso de {} é {}.'.format(fj , r))
#if fj == r:
    #print('Temos um palíndromo!')
#else:
    #print('A frase não é um palíndromo.')
