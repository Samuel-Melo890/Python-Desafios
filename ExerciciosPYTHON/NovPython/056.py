from module.interface import *
from os import system

system('cls')
menu('List Comprehension Nomes')

mulheres = ['Jeanne', 'Yor', 'Gine', 'Artoria', 'Mordred', 'Grey', 'Nero', 'Juvia', 'Rukia', 'Tatsumaki']
homens = ['Skull Knight', 'Guts', 'Bardock', 'Asta', 'Vegeta', 'Ichigo', 'Kazuma', 'Julius', 'Piccolo', 'Yami']

titulo('Homens 4 Letras')
homem_4l = [nome for nome in homens if len(nome) <= 4]
for pos, nome in enumerate(homem_4l):
    print(f'    {pos + 1} - {nome}')
system('pause')

system('cls')
titulo('Homens Duplas')
homens_dupla = [(nome[0], nome) for nome in homens]
for pos, tupla in enumerate(homens_dupla):
    print(f'{pos + 1} - {tupla[0]} | {tupla[1]}')
system('pause')

system('cls')
titulo('Homens Dupla Dict')
hom_dupla_dict = {tupla[0]: tupla[1] for tupla in homens_dupla}
for k, v in hom_dupla_dict.items():
    print(f'{k}: {v}')
print(f'Total: {len(hom_dupla_dict)} homens')
system('pause')

system('cls')
titulo('Homem Com Mulher')
h_m_zip = zip(homens, mulheres)
homem_mulher = {tupla[0]: tupla[1] for tupla in h_m_zip}
cont = 1
for homem, mulher in homem_mulher.items():
    print(f'{cont} -> {homem} S2 {mulher}')
    cont += 1
print(f'Total: {len(homem_mulher)} casais')
system('pause')

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
