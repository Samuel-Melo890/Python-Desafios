from module.interface import menu
from os import system

system('cls')
menu('Tuples Dictionary Comprehension')

l = [('Jeanne', 19), ('Samuel', 18), ('Gustavo', 24), ('Veda', 50)]

nome_idade = {k[0]: k[1] for k in l}
for k, v in nome_idade.items():
    print(f'\033[32m{k:.<15}\033[m\033[35m{v} anos\033[m')
