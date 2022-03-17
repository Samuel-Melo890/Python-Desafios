print('='*8,'Classe Pessoa','='*8)
from module import interface
from time import sleep

class Pessoa():
    def __init__(self, nome, idade, peso , altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos=0):
        m = 0
        for a in range(0, anos):
            if self.idade < 21:
                self.altura += 0.005
                m += 0.005
            self.idade += 1
        print(f'\033[35m{self.nome}\033[m envelheceu {anos} anos, agora ele(a) tem {self.idade} anos de idade.\nEle(a) cresceu {m:.3f}m, agora ele(a) tem {self.altura:.2f}m de altura.')
    def engordar(self, kg=0):
        if kg < 0:
            kg = -kg
        self.peso += kg
        print(f'\033[35m{self.nome}\033[m engordou {kg}kg, agora ele(a) tem {self.peso:.1f}kg de peso.')
    def emagrecer(self, kg=0):
        if kg < 0:
            kg = -kg
        self.peso -= kg
        print(f'\033[35m{self.nome}\033[m emagreceu {kg}kg, agora ele(a) tem {self.peso:.1f}kg de peso.')
    def crescer(self, cm=0):
        c = cm / 100
        self.altura += c
        print(f'\033[35m{self.nome}\033[m creceu {cm}cm, agora ele(a) tem {self.altura:.2f}m de altura. ')


interface.menu('Banco de Dados Pessoais')
print('Dê-me os dados pessoais de uma pessoa:')

while True:
    try:
        nome  = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        peso = float(input('Peso(kg): '))
        altura = float(input('Altura(m): '))
    except (ValueError, TypeError):
        print('\033[31mValores dados não válidos!\033[m')
    except KeyboardInterrupt:
        print('\033[36mValor não fornecido!\033[m')
    else:
        p = Pessoa(nome, idade, peso, altura)
        break

sleep(1.5)
while True:
    interface.titulo('Modificação')
    op = interface.options('Envelhecer', 'Engordar', 'Emagrecer', 'Crescer', 'Sair do programa')
    if op == 1:
        anos = int(input('Quantos anos deseja envelhecer a pessoa? '))
        p.envelhecer(anos)
        sleep(3)
    elif op == 2:
        kg = float(input('Em quantos kg deseja engordá-la? '))
        p.engordar(kg)
        sleep(2)
    elif op == 3:
        kg = float(input('Em quantos kg deseja emagrece-la? '))
        p.emagrecer(kg)
        sleep(2)
    elif op == 4:
        cm = int(input('Quantos cm quer que ela cresça? '))
        p.crescer(cm)
        sleep(2)
    else:
        interface.titulo('Saindo do Programa...')
        sleep(2)
        break
print('\033[36mPrograma Finalizado!\033[m')
