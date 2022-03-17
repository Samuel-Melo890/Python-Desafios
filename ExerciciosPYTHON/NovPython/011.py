print('='*8,'Classe Bomba de Combustível','='*8)
from module.interface import *
from time import sleep

class BombaCombustivel():
    def __init__(self, tipoCombts, valorLitro, qtdCombts):
        self.tipo = tipoCombts
        self.valorlit = valorLitro
        self.qtdCombts = QuantidadeCombts(qtdCombts)
    def abastecer_valor(self, valor):
        lit = valor / self.valorlit
        print(f'Com R${valor:.2f}, foram abastecidos \033[35m{lit} litros\033[m de \033[36m{self.tipo.title()}\033[m no veículo.')
        return lit
    def abastecer_litro(self, litros):
        valor = litros * self.valorlit
        print(f'O valor a ser pago por \033[35m{litros} litros\033[m de \033[36m{self.tipo.title()}\033[m é de R${valor:.2f}.')
    def alter_valorlit(self, novoValor):
        self.valorlit = novoValor
    def alter_Combts(self, novoTipo):
        self.tipo = novoTipo

class QuantidadeCombts():
    def __init__(self, qtdCombts):
        self.qtdCombts = qtdCombts
    def alter_qtdCombts(self, novaQtd):
        self.qtdCombts += novaQtd

menu('Posto do Seu João')
while True:
    try:
        tc = str(input('Qual o tipo de combustível que deseja? ')).strip().title()
    except KeyboardInterrupt:
        print('\033[36mDado não fornecido!\033[m')
    else:
        bomba = BombaCombustivel(tc, 4, 30)
        break

while True:
    titulo('Opções')
    op = options('Alterar Combustível', 'Abastecer Por valor', 'Abastecer por Litro', 'Mostrar Quantidade de Combustível', 'SAir do Posto')
    if op == 1:
        tc = str(input('Qual o novo tipo de combustível? ')).strip().title()
        bomba.alter_Combts(tc)
        print(f'O tipo do combustível foi alterado para \033[36m{tc}\033[m!')
        sleep(2)
    elif op == 2:
        valor = float(input('Qual o valor a ser abastecido? R$'))
        litro = bomba.abastecer_valor(valor)
        bomba.qtdCombts.alter_qtdCombts(-litro)
        sleep(2)
    elif op == 3:
        litro = float(input(f'Quantos litros de \033[36m{bomba.tipo}\033[m deseja abastecer? '))
        bomba.abastecer_litro(litro)
        bomba.qtdCombts.alter_qtdCombts(-litro)
        sleep(2)
    elif op == 4:
        print(f'A quantidade de combustível restante na bomba é de \033[35m{bomba.qtdCombts.qtdCombts} litros\033[m.')
        sleep(2)
    else:
        titulo('Saindo do Posto...')
        sleep(2)
        break
print('\033[36mPrograma Finalizado!\033[m')
