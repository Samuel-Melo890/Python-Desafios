print('='*8,'Classe Usuário','='*8)

class Usuario():
    def __init__(self, Fname, Lname, idade, cidade, hobby):
        self.Fname = Fname
        self.Lname = Lname
        self.idade = idade
        self.cidade = cidade
        self.hobby = hobby
    def descricao(self):
        print(f'Primeiro nome: {self.Fname.title()}\n\
Ultimo nome: {self.Lname.title()}\n\
Idade: {self.idade} anos\n\
Cidade: {self.cidade.title()}\n\
Hobby: {self.hobby.title()}')
    def saudacao(self):
        print(f'Olá \033[36m{self.Fname.title()}\033[m! Seja bem vindo(a)!')


print('')
user1 = Usuario('Jailson', 'Peludo', 40, 'Cidade da Delícia', 'Deixar o Oco')
user1.saudacao()
user1.descricao()
print('')

user2 = Usuario('Lloyd', 'Forger', 25, 'Berlim', 'Espião')
user2.saudacao()
user2.descricao()
print('')

user3 = Usuario('Yor', 'Briar', 25, 'Berlim', 'Assassina')
user3.saudacao()
user3.descricao()
