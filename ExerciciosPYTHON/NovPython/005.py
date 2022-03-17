print('='*8,'Início de Classes','='*8)

class Restaurante():
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo = tipo_cozinha
    def descrição(self):
        print(f'Nome: {self.nome.title()}')
        print(f'Tipo de Cozinha: {self.tipo.title()}')
    def res_aberto(self):
        print(f'\033[32mO restaurante {self.nome.title()} está aberto!\033[m')

r = Restaurante('Zeca Lanches', 'Italiana')
print(r.nome)
print(r.tipo)
r.descrição()
r.res_aberto()
