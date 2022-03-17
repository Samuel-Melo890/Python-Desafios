print('='*8,'Três Restaurantes','='*8)

class Restaurante():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    def descrição(self):
        print(f'Nome do restaurante: {self.nome.title()}')
        print(f'Tipo de cozinha: {self.tipo.title()}')
    def aberto(self):
        print(f'\033[32mO restaurante {self.nome.title()} está aberto!\033[m')


rest1 = Restaurante('Maria Lanches', 'Fast Food')
rest1.descrição()

rest2 = Restaurante('Sorveteria do Luís', 'Sorvetes e Gelados')
rest2.descrição()

rest3 = Restaurante('Churrascaria do seu Zé', 'Carne')
rest3.descrição()
