print('='*8,'Contagem Regressiva','='*8)

from time import sleep
for n in range(10, -1, -1):
    print('{}{}{}'.format('\033[7;1;41m',n,'\033[m'))
    sleep(1)
print('QUE COMECEM OS FOGOS!!!!')
