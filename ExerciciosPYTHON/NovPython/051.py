from module.interface import menu
from os import system

system('cls')
menu('Complemento a Orientação a Objetos 3')

class BaseDeDados():
    def __init__(self):
        self.dados = {}
    
    def inserir_cliente(self, id: int, nome: str):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})
    def listar_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

b = BaseDeDados()
b.inserir_cliente(1, 'Jeanne')
b.inserir_cliente(2, 'Skull Knight')
b.listar_clientes()
print(b.dados)
