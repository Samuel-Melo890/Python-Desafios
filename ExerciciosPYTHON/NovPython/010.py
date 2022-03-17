print('='*8,'Classe Mamaco','='*8)
from module import interface
from time import sleep

class Mamaco():
    def __init__(self, nome, bucho=20):
        self.nome = nome
        if bucho > 100 or bucho < 0:
            bucho = 20
        self.bucho = bucho
    def comer(self, comida='Banana'):
        print(f'O Mamaco \033[36m{self.nome}\033[m comeu \033[35m{comida.title()}\033[m!')
    def verBucho(self):
        print(f'O bucho do Mamaco \033[36m{self.nome}\033[m está em: ', end = '')
        if self.bucho <= 20:
            print(f'\033[31m{self.bucho}%\033[m <\033[31mFaminto\033[m>')
        elif self.bucho <= 60:
            print(f'\033[33m{self.bucho}%\033[m <\033[33mCom Fome\033[m>')
        else:
            print(f'\033[32m{self.bucho}%\033[m <\033[32mSatisfeito\033[m>')
    def digerir(self, comida='Banana'):
        print(f'Mamaco \033[36m{self.nome}\033[m está digerindo \033[35m{comida.title()}\033[m...')
        if comida in "Mamaco":
            self.bucho += 100
        else:
            self.bucho += 20


while True:
    interface.menu('Mamacos Interativos')
    
    try:
        n1 = str(input('Nome do primeiro Mamaco: ')).strip().title()
        n2 = str(input('Nome do segundo Mamaco: ')).strip().title()
    except KeyboardInterrupt:
        print('\033[36mDado não fornecido!\033[m')
    else:
        m1 = Mamaco(n1)
        m2 = Mamaco(n2)
        sleep(1)
        break

c = ['Banana', 'Folha', 'Inseto']
while True:
    interface.titulo('Interação')
    op = interface.options('Dar comida a Mamaco', 'Ver bucho do Mamaco', 'Canibalismo de Mamacos', 'SAir do programa')
    if op == 1:
        sleep(1)
        interface.titulo('Qual Mamaco?')
        e = interface.options(f'{m1.nome}', f'{m2.nome}')
        if e == 1:
            comida = interface.options(f'{c[0]}', f'{c[1]}', f'{c[2]}')
            m1.comer(c[comida - 1])
            m1.digerir(c[comida - 1])
        else:
            comida = interface.options(f'{c[0]}', f'{c[1]}', f'{c[2]}')
            m2.comer(c[comida - 1])
            m2.digerir(c[comida - 1])
        sleep(2)
    elif op == 2:
        sleep(1)
        interface.titulo('Qual Mamaco?')
        e = interface.options(f'{m1.nome}', f'{m2.nome}')
        if e == 1:
            m1.verBucho()
        else:
            m2.verBucho()
        sleep(2)
    elif op == 3:
        interface.titulo('Qual deve Viver?')
        e = interface.options(f'{m1.nome}', f'{m2.nome}')
        if e == 1:
            m1.comer('Mamaco')
            m1.digerir('Mamaco')
            print(f'\033[31m{m1.nome} está satisfeito(bucho {m1.bucho}%) com o sangue derramado de {m2.nome}\033[m')
            del m2
        else:
            m2.comer('Mamaco')
            m2.digerir('Mamaco')
            print(f'\033[31m{m2.nome} está satisfeito(bucho {m2.bucho}%) com o sangue derramado de {m1.nome}\033[m')
            del m1
        sleep(2)
        break
    else:
        interface.titulo('Saindo do Programa...')
        sleep(2)
        break
print('\033[36mPrograma Finalizado!\033[m')
