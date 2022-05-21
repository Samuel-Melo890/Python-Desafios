from os import system
from module.interface import *
from time import sleep

system('cls')
print('='*8,'Carros','='*8)

class Carro():
    def __init__(self, nome, potencia, velmax):
        self.nome = nome
        self.pot = potencia
        self.velmax = velmax
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def info(self):
        self.estado = 'Desligado'
        if self.ligado == True:
            self.estado = 'Ligado'
        print(f'Informações do carro \033[36m{self.nome}\033[m:')
        print(f'    Nome...............{self.nome}')
        print(f'    Potência...........{self.pot} Watts')
        print(f'    Vel.Máxima.........{self.velmax} km/h')
        print(f'    Estado.............{self.estado}')
    

carros = []

while True:
    menu('Automobilística João')
    print(f'Quantidade de Carros: {len(carros)}')
    op = options('Criar um novo carro', 'Ver informações do carro', 'Excluir carro', 'Ligar carro', 'Desligar carro', 'Listar os carros', 'Sair do programa')
    if 1 <= op <= 6:
        while True:
            sleep(1)
            try:
                if op == 1:
                    titulo('Novo Carro')
                    nome = str(input('Nome do carro: ')).strip().title()
                    if len(nome) == 0:
                        print('\033[36mPor favor crie um nome para o seu carro!\033[m')
                        continue
                    pot = float(input('Potência do carro: '))
                    velmax = float(input('Velocidade Máxima: '))
                    
                    car = Carro(nome, pot, velmax)
                    carros.append(car)
                    
                    sleep(0.5)
                    print('\033[32mCarro adicionado com sucesso!\033[m')
                elif op == 2:
                    ord_carro = int(input('Qual o número do carro que deseja ver? '))
                    
                    if ord_carro > len(carros) or ord_carro < 1:
                        print('>> \033[34mQuantidade de carros vazia ou carro não encontrado.\033[m')
                    
                    else:
                        for o, car in enumerate(carros):
                            if ord_carro == (o + 1):
                                car.info()
                elif op == 3:
                    ord_carro = int(input('Qual o número do carro que deseja excluir? '))
                    
                    if ord_carro > len(carros) or ord_carro < 1:
                        print('>> \033[34mCarro não encontrado\033[m')
                    
                    else:
                        sleep(0.5)
                        r = ' '
                        while r not in 'SN':
                            r = str(input(f'Deseja excluir o carro {carros[ord_carro - 1].nome}? [S/N] ')).strip().upper()[0]
                        
                        if r in 'S':
                            del carros[ord_carro - 1]
                            sleep(0.5)
                            print('\033[32mCarro Deletado com Sucesso!\033[m')
                        else:
                            print(f'Carro \033[36m{carros[ord_carro - 1].nome}\033[m será mantido.')
                elif op == 4:
                    ord_carro = int(input('Qual o número do carro que deseja ligar? '))
                    
                    if ord_carro > len(carros) or ord_carro < 1:
                        print('>> \033[34mCarro não encontrado.\033[m')
                    
                    else:
                        carros[ord_carro - 1].ligar()
                        sleep(0.5)
                        print(f'\033[32mCarro {carros[ord_carro - 1].nome} foi ligado!\033[m')
                elif op == 5:
                    ord_carro = int(input('Qual o número do carro que deseja desligar? '))
                    
                    if ord_carro > len(carros) or ord_carro < 1:
                        print('>> \033[34mCarro não encontrado.\033[m')
                    
                    else:
                        carros[ord_carro - 1].desligar()
                        sleep(0.5)
                        print(f'\033[32mCarro {carros[ord_carro - 1].nome} foi desligado!\033[m')
                else:
                    titulo('Lista do Carros')
                    if len(carros) == 0:
                        print('>> \033[34mLista de carros vazia.\033[m')
                    else:
                        for o, c in enumerate(carros):
                            print(f'Número: {o + 1} | Nome: {c.nome}')
                            sleep(0.5)
            except(ValueError, TypeError):
                print('\033[31mERRO! Por favor insira um número inteiro!\033[m')
            except KeyboardInterrupt:
                print('\033[31mERRO! Por favor preencha os campos dados!\033[m')
            else:
                sleep(2)
                break
    else:
        titulo('Saindo do Programa...')
        sleep(2)
        break
print('\033[36mPrograma Finalizado!\033[m')
