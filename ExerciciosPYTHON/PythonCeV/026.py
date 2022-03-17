print('='*8,'Primeira e Ultima Ocorrencia de uma String','='*8)

f = str(input('Digite uma frase qualquer:')).strip().lower()
l = str(input('Escolha uma letra qualquer:')).strip().lower()
qva = f.count(l)
ppa = f.find(l)
upa = f.rfind(l)
from time import sleep
print('Analisando a sua string...')
sleep(2)
print('''A letra {} aparece {} vez(es).
Ela aparece pela primeira vez no caractere {}.
E ela aparece pela ultima vez no caractere {}.'''.format(l,qva,ppa,upa))
